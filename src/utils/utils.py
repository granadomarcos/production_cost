""" Utils class from the project"""
import json
import os
import shutil
from datetime import date, datetime
import pandas as pd
import logging
import requests as req
from pandas import DataFrame
import urllib
from tqdm import tqdm
import urllib.parse as urlparse


class Utils(object):
    """ Utils class from the project"""

    @staticmethod
    def create_work_dir():
        logging.info("Criando diretorios base")

        dirs = ['files/raw', 'files/trusted', 'files/refined']
        for directory in dirs:
            if os.path.exists(directory):
                shutil.rmtree(directory)
            os.makedirs(directory)

        logging.info("Diretorios criados.")


    @staticmethod
    def get_products(produtos: list):

        listaprodutos = []
        for produto in produtos:
            listaprodutos.append(produto[1])

        produtos = [urllib.parse.quote_plus(produto) for produto in listaprodutos]
        return produtos

    @staticmethod
    def get_urls_years(produtos: list):
        urls_years = []
        for i in produtos:
            urls_years.append('https://pentahoportaldeinformacoes.conab.gov.br/pentaho/plugin/cda/api/doQuery?'
                              'paramempreendimento=%5BTipo+Empreendimento%5D.%5BTODOS%5D&paramproduto=%5BProduto%5D.%5B{}%5D&'
                              'paramsafra=%5BTipo+Safra%5D.%5BTODAS%5D&paramclassificacao=%5BProduto+Classificacao%5D.%'
                              '5BTODAS%5D&path=%2Fhome%2FSIAGRO%2FCustoProducao.cda&dataAccessId=anoMDX&outputIndexId=1&'
                              'pageSize=0&pageStart=0&sortBy=&paramsearchBox='.format(i))
        return urls_years

    @staticmethod
    def get_list_product_year(lista_de_anos: list):

        listaparaanos = []
        for produto in lista_de_anos:
            sublista = []
            for item in range(len(produto)):
                sublista.append(produto[item][1])
            listaparaanos.append(sublista)
        return listaparaanos

    @staticmethod
    def get_list_product_year_pair(listaparaanos: list, produtos: list):
        lista_produto_ano = []
        for anos, produto in zip(listaparaanos, produtos):
            for ano in anos:
                item = {'ano': ano, 'produto': produto}
                lista_produto_ano.append(item)
        return lista_produto_ano

    @staticmethod
    def product_year_filtered(lista_produto_ano: list):

        previous_year = date.today().year - 1
        current_year = date.today().year

        dfprodutos = pd.DataFrame(lista_produto_ano)

        dfprodutos_previuos = dfprodutos.loc[(dfprodutos['ano'] == str(previous_year))]

        dfprodutos_current = dfprodutos.loc[(dfprodutos['ano'] == str(current_year))]

        data = [dfprodutos_current, dfprodutos_previuos]
        df_produtos_current_previous = pd.concat(data, ignore_index=False, sort=True)
        dfprodutos = df_produtos_current_previous.sort_values(by='produto')

        return dfprodutos


    @staticmethod
    def create_urls_for_months(lista_produtos: list, anos: list):
        urls_meses = []
        for produto, ano in zip(lista_produtos, anos):
            urls_meses.append('https://pentahoportaldeinformacoes.conab.gov.br/pentaho/plugin/cda/api/doQuery?'
                              'paramempreendimento=%5BTipo+Empreendimento%5D.%5BTODOS%5D&paramproduto=%5BProduto%'
                              '5D.%5B{}%5D&paramsafra=%5BTipo+Safra%5D.%5BTODAS%5D&paramano=%5BAno%5D.%5B{}%5D&'
                              'paramclassificacao=%5BProduto+Classificacao%5D.%5BTODAS%5D&path=%2Fhome%2FSIAGRO%'
                              '2FCustoProducao.cda&dataAccessId=mesMDX&outputIndexId=1&pageSize=0&pageStart=0&'
                              'sortBy=&paramsearchBox='.format(produto, ano))
        return urls_meses

    @staticmethod
    def create_list_for_months(lista_de_meses: list):
        lista_para_meses = []
        for mes in lista_de_meses:
            sublista = []
            for item in range(len(mes)):
                sublista.append(mes[item][1])
            lista_para_meses.append(sublista)
        return lista_para_meses

    @staticmethod
    def create_list_product_year_month(anos: list, lista_produtos: list, lista_para_meses: list):
        lista_produto_ano_mes = []
        for ano, produto, mes in zip(anos, lista_produtos, lista_para_meses):
            for mesexistente in mes:
                item = {'ano': ano, 'produto': produto, 'mes': mesexistente}
                lista_produto_ano_mes.append(item)
        return lista_produto_ano_mes

    @staticmethod
    def getlist_urls_cities(lista_de_produtos: list, lista_de_anos: list, lista_de_meses: list ):
        urls_municipios = []
        for i in zip(lista_de_produtos, lista_de_anos, lista_de_meses):
            urls_municipios.append('https://pentahoportaldeinformacoes.conab.gov.br/pentaho/plugin/cda/api/doQuery?'
                                   'paramempreendimento=%5BTipo+Empreendimento%5D.%5BTODOS%5D&paramproduto=%'
                                   '5BProduto%5D.%5B{}%5D&paramsafra=%5BTipo+Safra%5D.%5BTODAS%5D&paramano=%5BAno%'
                                   '5D.%5B{}%5D&parammes=%5BMes%5D.%5B{}%5D&paramclassificacao=%'
                                   '5BProduto+Classificacao%5D.%5BTODAS%5D&path=%2Fhome%2FSIAGRO%'
                                   '2FCustoProducao.cda&dataAccessId=custoVariavelMunicipioProdutividade&'
                                   'outputIndexId=1&pageSize=0&pageStart=0&sortBy=&paramsearchBox='.format(i[0],
                                                                                                           i[1],i[2]))
        return urls_municipios

    @staticmethod
    def create_cities_list(citieslist: list):
        lista_de_municipios = []
        for municipio in citieslist:
            sublista = []
            for item in range(len(municipio)):
                sublista.append(municipio[item][0])
            lista_de_municipios.append(sublista)
        return lista_de_municipios

    @staticmethod
    def createproduct_year_month_city_list(lista_de_anos: list, lista_de_produtos: list,
                                           lista_de_meses: list, lista_de_municipios: list):
        lista_produto_ano_mes_municipio = []
        for ano, produto, mes, municipios in zip(lista_de_anos, lista_de_produtos, lista_de_meses,
                                                 lista_de_municipios):
            for municipio in municipios:
                item = {'ano': ano, 'produto': produto, 'mes': mes, 'municipio': municipio}
                lista_produto_ano_mes_municipio.append(item)
        return lista_produto_ano_mes_municipio

    @staticmethod
    def get_urls_to_ingest(lista_de_produtos: list, lista_de_anos: list,
                           lista_de_meses: list, lista_de_municipios: list):
        urls = []
        for i in zip(lista_de_produtos, lista_de_anos, lista_de_meses, lista_de_municipios):
            urls.append(
                "https://pentahoportaldeinformacoes.conab.gov.br/pentaho/plugin/cda/api/doQuery?"
                "paramempreendimento=%5BTipo+Empreendimento%5D.%5BTODOS%5D&paramproduto=%5BProduto%5D.%5B{}%"
                "5D&paramsafra=%5BTipo+Safra%5D.%5BTODAS%5D&paramano=%5BAno%5D.%5B{}%5D&parammes=%"
                "5BMes%5D.%5B{}%5D&parammunicipio={}&paramtipoCusto=CUSTO+VARI%C3%81VEL&path=%2Fhome%"
                "2FSIAGRO%2FCustoProducao.cda&dataAccessId=custoDetalhadoMunic&outputIndexId=1&"
                "pageSize=0&pageStart=0&sortBy=&paramsearchBox=".format(i[0], i[1], i[2], i[3]))
        return urls

    @staticmethod
    def get_df_from_url_data(urls: list, headers: dict) -> pd.DataFrame:
        """ Creates a data frame for each data came from the URLs requested

        Parameters
        ----------
        urls : list
            urls to  ingest
        headers : dict
            auth

        Returns
        -------
        DataFrame
            DataFrame with all data to ingest
        """
        df = DataFrame()

        for url in urls:
            resp = req.post(url, headers=headers)
            if resp.status_code == req.codes.OK:
                dataparam = dict(urllib.parse.parse_qsl(urllib.parse.urlparse(url).query))
                dfparamurl = pd.DataFrame(dataparam, index=[0])
                dfparamurl['key'] = 1
                data = json.loads(resp.content)
                data = data.get('resultset')
                data = pd.DataFrame(data)
                data['key'] = 1
                data = pd.merge(data, dfparamurl, on='key')
                data = data.drop(columns='key')
                data['ingestion_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                df = pd.concat([df, data])
            else:
                continue
        return df

    # * Discuss about a writer object to avoid the code repeat
    @staticmethod
    def write_file_container(df: DataFrame, pathroot: str) -> list:
        """ Writes a dataframe in the container as a CSV file

        Parameters
        ----------
        df : DataFrame
            Data to be written
        pathroot : str
            Where the data will be stored

        Returns
        -------
        list
            List with all the paths used to save the respective data
        """
        pathenvir = f"files/{pathroot}/conab/custovariavel/"

        df['year'] = df['paramano'].str.extract('(\d+)')
        df['month'] = df['parammes'].str[7:-1]
        df[['year', 'month']] = df[['year', 'month']].astype("string")

        monthtext = df['month']
        monthtext = monthtext.astype("string")
        monthtext = monthtext.to_string(index=False).split('\n')
        monthtext = [mes.strip() for mes in monthtext]
        monthlist = [Utils.month_numeric_format(month) for month in monthtext]

        df['monthnumeric'] = monthlist
        df['monthnumeric'] = df['monthnumeric'].astype("string")
        df['yearmonthnumeric'] = df['year'] + df['monthnumeric']

        pathlist = []
        size = len(df['yearmonthnumeric'].unique())
        with tqdm(total=size) as pbar:
            pbar.set_description(f"Writing the data in the container paths ({pathroot} layer)")
            for yearmonth, df_filtrado in df.groupby('yearmonthnumeric'):
                year = str(yearmonth)[0:4]
                month = str(yearmonth)[4:6]
                pathfull = pathenvir + year + '/' + month
                fileconabcustovariavel = pathfull + '/' + 'conab_custovariavel_' + year + '_' + month + '.csv'

                if not os.path.exists(pathfull):
                    os.makedirs(pathfull)

                df_filtrado.to_csv(fileconabcustovariavel, sep=';', header=True, encoding='utf-8', index=False)
                pathlist.append(fileconabcustovariavel)
                pbar.update(1)
        return pathlist

    @staticmethod
    def month_numeric_format(monthstr: str) -> str:
        """ Transforms the month name into a number string

        Parameters
        ----------
        monthstr : str
            Month name

        Returns
        -------
        str
            Month number
        """
        month_number = {
            'JANEIRO': '01',
            'FEVEREIRO': '02',
            'MARÇO': '03',
            'ABRIL': '04',
            'MAIO': '05',
            'JUNHO': '06',
            'JULHO': '07',
            'AGOSTO': '08',
            'SETEMBRO': '09',
            'OUTUBRO': '10',
            'NOVEMBRO': '11',
            'DEZEMBRO': '12'
        }
        if monthstr in month_number:
            return_monthnumber = month_number[monthstr]
        else:
            return_monthnumber = '00'

        return return_monthnumber

    @staticmethod
    def write_to_trusted(df: DataFrame) -> pd.DataFrame:  # ? Change the function name
        """Treat the data to be stored in the trusted layer

        Parameters
        ----------
        df : DataFrame
            Data to be transformed

        Returns
        -------
        pd.DataFrame
            Data transformed
        """
        dftrusted = df.copy()

        dftrusted['year'] = dftrusted['paramano'].str.extract('(\d+)')
        dftrusted['month'] = dftrusted['parammes'].str[7:-1]
        dftrusted[['year', 'month']] = dftrusted[['year', 'month']].astype("string")
        dftrusted['product'] = dftrusted['paramproduto'].str[11:-1]
        dftrusted['uf'] = dftrusted['parammunicipio'].str[-2:]
        dftrusted['city'] = dftrusted['parammunicipio'].str[:-3]

        drop_list = ["paramempreendimento", "path", "dataAccessId", "outputIndexId", "pageSize", "pageStart",
                     "paramproduto"]
        dftrusted.drop(drop_list, axis=1, inplace=True)
        return dftrusted