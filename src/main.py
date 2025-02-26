import os
import requests as req
import logging
from datetime import date, datetime
import urllib
import pandas as pd
import json
import sys
from utils.utils import Utils

class Main(object):
    def __init__(self):
        # Initialize method
        pass

    @staticmethod
    def run():
        
        try:

            cwd = os.getcwd()
            path = os.path.dirname(cwd)
            projeto = os.path.basename(path)

            # Configuração do logging
            logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


            logging.info("Processo iniciado.")

            Utils.create_work_dir()

            headers = {
                'Authorization': 'Basic cGVudGFobzpwYXNzd29yZA==',
                'Referer': 'https://pentahoportaldeinformacoes.conab.gov.br/pentaho/api/repos/:'
                           'home:SIAGRO:CustoProducao.wcdf/generatedContent?userid=pentaho&password=password',
                'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}

            url_produtos = 'https://pentahoportaldeinformacoes.conab.gov.br/pentaho/plugin/cda/api/doQuery?' \
                           'paramempreendimento=%5BTipo+Empreendimento%5D.%5BTODOS%5D&path=%2Fhome%2FSIAGRO%' \
                           '2FCustoProducao.cda&dataAccessId=produto&outputIndexId=1&pageSize=0&pageStart=0&' \
                           'sortBy=&paramsearchBox='

            response = req.post(url_produtos, headers=headers)
            objeto = json.loads(response.text)
            produtos = objeto['resultset']

            produtos = Utils.get_products(produtos=produtos)

            url_years = Utils.get_urls_years(produtos=produtos)

            lista_de_anos = []
            for url in url_years:
                resp = req.post(url, headers=headers)
                if resp.status_code == req.codes.OK:
                    data = json.loads(resp.text)
                    lista_de_anos.append(data['resultset'])
                else:
                    continue

            listaparaanos = Utils.get_list_product_year(lista_de_anos=lista_de_anos)
            lista_produto_ano = Utils.get_list_product_year_pair(listaparaanos=listaparaanos, produtos=produtos)
            dfprodutos = Utils.product_year_filtered(lista_produto_ano=lista_produto_ano)
            # Para histórico
            # dfprodutos = pd.DataFrame(lista_produto_ano) 

            anos = list(dfprodutos['ano'])
            lista_produtos = list(dfprodutos['produto'])

            urls_meses = Utils.create_urls_for_months(lista_produtos=lista_produtos, anos=anos)

            lista_de_meses = []
            for url in urls_meses:
                resp = req.post(url, headers=headers)
                if resp.status_code == req.codes.OK:
                    data = json.loads(resp.text)
                    lista_de_meses.append(data['resultset'])
                else:
                    continue

            lista_para_meses = Utils.create_list_for_months(lista_de_meses=lista_de_meses)

            lista_produto_ano_mes = Utils.create_list_product_year_month(anos=anos, lista_produtos=lista_produtos,
                                                                            lista_para_meses=lista_para_meses)

            dataframe = pd.DataFrame(lista_produto_ano_mes)
            lista_de_meses = dataframe['mes']
            lista_de_meses = [urllib.parse.quote_plus(mes) for mes in lista_de_meses]
            lista_de_produtos = dataframe['produto']
            lista_de_anos = dataframe['ano']

            urls_municipios = Utils.getlist_urls_cities(lista_de_produtos=lista_de_produtos,
                                                        lista_de_anos=lista_de_anos, lista_de_meses=lista_de_meses)

            citieslist = []
            for url in urls_municipios:
                resp = req.post(url, headers=headers)
                if resp.status_code == req.codes.OK:
                    data = json.loads(resp.text)
                    citieslist.append(data['resultset'])
                else:
                    continue

            lista_de_municipios = Utils.create_cities_list(citieslist=citieslist)

            lista_produto_ano_mes_municipio = Utils.createproduct_year_month_city_list(lista_de_anos=lista_de_anos,
                                                                                       lista_de_produtos=lista_de_produtos,
                                       lista_de_meses=lista_de_meses, lista_de_municipios=lista_de_municipios)

            dataframe_lista_produto_ano_mes_municipio = pd.DataFrame(lista_produto_ano_mes_municipio)
            lista_de_meses = dataframe_lista_produto_ano_mes_municipio['mes']
            lista_de_produtos = dataframe_lista_produto_ano_mes_municipio['produto']
            lista_de_anos = dataframe_lista_produto_ano_mes_municipio['ano']
            lista_de_municipios = dataframe_lista_produto_ano_mes_municipio['municipio']
            lista_de_municipios = [urllib.parse.quote_plus(municipio) for municipio in lista_de_municipios]

            urls = Utils.get_urls_to_ingest(lista_de_produtos=lista_de_produtos, lista_de_anos=lista_de_anos,
                           lista_de_meses=lista_de_meses, lista_de_municipios=lista_de_municipios)

            if urls:
                logging.info(f"Found {len(urls)} items in the URLs list")
            else:
                logging.info("Not found list urls-api-conab-custovariavel")

            df = Utils.get_df_from_url_data(urls=urls, headers=headers)

            if df.empty:
                logging.info("Dataframe is empty")
            else:
                df.rename(columns={0: 'itemdecusto', 1: 'custovariavel'}, inplace=True)
                pathlists = Utils.write_file_container(df=df, pathroot="raw")

                dftrusted = Utils.write_to_trusted(df=df)

                pathlists = Utils.write_file_container(df=dftrusted, pathroot="trusted")

                logging.info(f"Pathlists {pathlists}")


            logging.info("Execution finished with success!")
        except Exception as error:
            logging.info("Error Description: " + str(error))


if __name__ == '__main__':
    main = Main()
    main.run()
