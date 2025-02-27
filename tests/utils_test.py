"""Módulo principal de testes"""
import unittest
from src.utils.utils import Utils
import os
import pandas as pd


headers = {
            'Authorization': 'Basic cGVudGFobzpwYXNzd29yZA==',
            'Referer': 'https://pentahoportaldeinformacoes.conab.gov.br/pentaho/api/repos/:'
                       'home:SIAGRO:CustoProducao.wcdf/generatedContent?userid=pentaho&password=password',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}

filename = "data.csv"

class UtilsTest(unittest.TestCase):

    def test_create_work_dir(self):
        dirs = ['src/files/raw', 'src/files/trusted', 'src/files/refined',
                'src/files/exploratory', 'src/files/features', 'src/files/sandbox']
        for directory in dirs:
            Utils.create_work_dir()
            assert os.path.exists(directory)

    def test_get_products(self):
        produtoref = ['ABACAXI', 'ACAI', 'ALGODAO+EM+PLUMA', 'AMENDOA+DE+ANDIROBA', 'AMENDOA+DE+BARU',
                      'AMENDOA+DE+CACAU', 'AMENDOIM', 'ARROZ', 'AVEIA', 'BANANA', 'BATATA', 'BATATA-DOCE', 'BORRACHA',
                      'BORRACHA+NATURAL', 'BURITI', 'CAFE', 'CANOLA', 'CARA', 'CASTANHA+DE+BABACU', 'CASTANHA+DE+CAJU',
                      'CASTANHA+DO+BRASIL', 'CEBOLA', 'CERA+DE+CARNAUBA', 'CEVADA', 'ERVA+MATE', 'FAVA+D%27ANTA',
                      'FEIJAO', 'GIRASSOL', 'GUARANA', 'INHAME', 'JUCARA', 'LARANJA', 'LICURI', 'MACA', 'MACAUBA',
                      'MAMONA+EM+BAGA', 'MANGABA', 'MEL+DE+ABELHA', 'MILHO', 'MURUMURU', 'PEQUI', 'PESSEGO', 'PIACAVA',
                      'PINHAO', 'PIRARUCU', 'PO+CERIFERO+DE+CARNAUBA', 'QUIABO', 'RAIZ+DE+MANDIOCA', 'SISAL', 'SOJA',
                      'SORGO+GRANIFERO', 'TANGERINA', 'TOMATE', 'TRIGO', 'TRITICALE', 'UMBU', 'UVA']

        produtos = [['[Produto].[ABACAXI]', 'ABACAXI'], ['[Produto].[ACAI]', 'ACAI'], ['[Produto].[ALGODAO EM PLUMA]', 'ALGODAO EM PLUMA'], ['[Produto].[AMENDOA DE ANDIROBA]', 'AMENDOA DE ANDIROBA'], ['[Produto].[AMENDOA DE BARU]', 'AMENDOA DE BARU'], ['[Produto].[AMENDOA DE CACAU]', 'AMENDOA DE CACAU'], ['[Produto].[AMENDOIM]', 'AMENDOIM'], ['[Produto].[ARROZ]', 'ARROZ'], ['[Produto].[AVEIA]', 'AVEIA'], ['[Produto].[BANANA]', 'BANANA'], ['[Produto].[BATATA]', 'BATATA'], ['[Produto].[BATATA-DOCE]', 'BATATA-DOCE'], ['[Produto].[BORRACHA]', 'BORRACHA'], ['[Produto].[BORRACHA NATURAL]', 'BORRACHA NATURAL'], ['[Produto].[BURITI]', 'BURITI'], ['[Produto].[CAFE]', 'CAFE'], ['[Produto].[CANOLA]', 'CANOLA'], ['[Produto].[CARA]', 'CARA'], ['[Produto].[CASTANHA DE BABACU]', 'CASTANHA DE BABACU'], ['[Produto].[CASTANHA DE CAJU]', 'CASTANHA DE CAJU'], ['[Produto].[CASTANHA DO BRASIL]', 'CASTANHA DO BRASIL'], ['[Produto].[CEBOLA]', 'CEBOLA'], ['[Produto].[CERA DE CARNAUBA]', 'CERA DE CARNAUBA'], ['[Produto].[CEVADA]', 'CEVADA'], ['[Produto].[ERVA MATE]', 'ERVA MATE'], ["[Produto].[FAVA D'ANTA]", "FAVA D'ANTA"], ['[Produto].[FEIJAO]', 'FEIJAO'], ['[Produto].[GIRASSOL]', 'GIRASSOL'], ['[Produto].[GUARANA]', 'GUARANA'], ['[Produto].[INHAME]', 'INHAME'], ['[Produto].[JUCARA]', 'JUCARA'], ['[Produto].[LARANJA]', 'LARANJA'], ['[Produto].[LICURI]', 'LICURI'], ['[Produto].[MACA]', 'MACA'], ['[Produto].[MACAUBA]', 'MACAUBA'], ['[Produto].[MAMONA EM BAGA]', 'MAMONA EM BAGA'], ['[Produto].[MANGABA]', 'MANGABA'], ['[Produto].[MEL DE ABELHA]', 'MEL DE ABELHA'], ['[Produto].[MILHO]', 'MILHO'], ['[Produto].[MURUMURU]', 'MURUMURU'], ['[Produto].[PEQUI]', 'PEQUI'], ['[Produto].[PESSEGO]', 'PESSEGO'], ['[Produto].[PIACAVA]', 'PIACAVA'], ['[Produto].[PINHAO]', 'PINHAO'], ['[Produto].[PIRARUCU]', 'PIRARUCU'], ['[Produto].[PO CERIFERO DE CARNAUBA]', 'PO CERIFERO DE CARNAUBA'], ['[Produto].[QUIABO]', 'QUIABO'], ['[Produto].[RAIZ DE MANDIOCA]', 'RAIZ DE MANDIOCA'], ['[Produto].[SISAL]', 'SISAL'], ['[Produto].[SOJA]', 'SOJA'], ['[Produto].[SORGO GRANIFERO]', 'SORGO GRANIFERO'], ['[Produto].[TANGERINA]', 'TANGERINA'], ['[Produto].[TOMATE]', 'TOMATE'], ['[Produto].[TRIGO]', 'TRIGO'], ['[Produto].[TRITICALE]', 'TRITICALE'], ['[Produto].[UMBU]', 'UMBU'], ['[Produto].[UVA]', 'UVA']]
        produtos = Utils.get_products(produtos=produtos)
        assert produtos.__eq__(produtoref)

    def test_get_urls_years(self):
        produtos = ['MILHO']
        urlref = ['https://pentahoportaldeinformacoes.conab.gov.br/pentaho/plugin/cda/api/doQuery?'
                  'paramempreendimento=%5BTipo+Empreendimento%5D.%5BTODOS%5D&paramproduto=%5BProduto%5D.%5BMILHO%5D&'
                  'paramsafra=%5BTipo+Safra%5D.%5BTODAS%5D&paramclassificacao=%5BProduto+Classificacao%5D.%'
                  '5BTODAS%5D&path=%2Fhome%2FSIAGRO%2FCustoProducao.cda&dataAccessId=anoMDX&outputIndexId=1&'
                  'pageSize=0&pageStart=0&sortBy=&paramsearchBox=']
        urls_years = Utils.get_urls_years(produtos=produtos)
        assert urls_years.__eq__(urlref)

    def test_get_list_product_year(self):
        lista_de_anos = [[['[Ano].[2022]', '2022'],
                          ['[Ano].[2021]', '2021'],
                          ['[Ano].[2020]', '2020'],
                          ['[Ano].[2019]', '2019']]]
        listaparaanosref = [['2022', '2021', '2020', '2019']]
        listaparaanos = Utils.get_list_product_year(lista_de_anos=lista_de_anos)
        assert listaparaanos.__eq__(listaparaanosref)

    def test_get_list_product_year_pair(self):
        lista_produto_anoref = [{'ano': '2022', 'produto': 'ABACAXI'},
                                 {'ano': '2021', 'produto': 'ABACAXI'},
                                 {'ano': '2020', 'produto': 'ABACAXI'},
                                 {'ano': '2019', 'produto': 'ABACAXI'}]
        listaparaanos = [['2022', '2021', '2020', '2019']]
        produtos = ['ABACAXI']
        lista_produto_ano = Utils.get_list_product_year_pair(listaparaanos=listaparaanos, produtos=produtos)
        assert lista_produto_ano.__eq__(lista_produto_anoref)

    def test_product_year_filtered(self):
        lista_produto_ano = [{'ano': '2022', 'produto': 'ABACAXI'},
                             {'ano': '2021', 'produto': 'ABACAXI'},
                             {'ano': '2020', 'produto': 'ABACAXI'},
                             {'ano': '2019', 'produto': 'ABACAXI'}]
        df = {'ano': [2022, 2021], 'produto': ['ABACAXI', 'ABACAXI']}
        dfprodutosref = pd.DataFrame(data=df)
        dfprodutos = Utils.product_year_filtered(lista_produto_ano=lista_produto_ano)
        dfprodutos = pd.DataFrame(data=dfprodutos)
        assert dfprodutos.equals(dfprodutosref.astype(str))

    def test_create_urls_for_months(self):
        anos = ['2022', '2021']
        lista_produtos = ['ABACAXI', 'ABACAXI']
        urls_mesesref = ['https://pentahoportaldeinformacoes.conab.gov.br/pentaho/plugin/cda/api/doQuery?paramempreendimento=%5BTipo+Empreendimento%5D.%5BTODOS%5D&paramproduto=%5BProduto%5D.%5BABACAXI%5D&paramsafra=%5BTipo+Safra%5D.%5BTODAS%5D&paramano=%5BAno%5D.%5B2022%5D&paramclassificacao=%5BProduto+Classificacao%5D.%5BTODAS%5D&path=%2Fhome%2FSIAGRO%2FCustoProducao.cda&dataAccessId=mesMDX&outputIndexId=1&pageSize=0&pageStart=0&sortBy=&paramsearchBox=',
                         'https://pentahoportaldeinformacoes.conab.gov.br/pentaho/plugin/cda/api/doQuery?paramempreendimento=%5BTipo+Empreendimento%5D.%5BTODOS%5D&paramproduto=%5BProduto%5D.%5BABACAXI%5D&paramsafra=%5BTipo+Safra%5D.%5BTODAS%5D&paramano=%5BAno%5D.%5B2021%5D&paramclassificacao=%5BProduto+Classificacao%5D.%5BTODAS%5D&path=%2Fhome%2FSIAGRO%2FCustoProducao.cda&dataAccessId=mesMDX&outputIndexId=1&pageSize=0&pageStart=0&sortBy=&paramsearchBox=']
        urls_meses = Utils.create_urls_for_months(lista_produtos=lista_produtos, anos=anos)
        assert urls_meses.__eq__(urls_mesesref)

    def test_create_list_for_months(self):

        lista_de_meses = [[['[Mes].[MARÇO]', 'MARÇO']], [['[Mes].[MARÇO]', 'MARÇO']]]
        lista_para_mesesref= [['MARÇO'], ['MARÇO']]
        lista_para_meses = Utils.create_list_for_months(lista_de_meses=lista_de_meses)

        assert lista_para_meses.__eq__(lista_para_mesesref)

    def test_create_list_product_year_month(self):
        anos = ['2022', '2021']
        lista_produtos = ['ABACAXI', 'ABACAXI']
        lista_para_meses = [['MARÇO'], ['MARÇO']]
        lista_produto_ano_mesref= [{'ano': '2022', 'produto': 'ABACAXI', 'mes': 'MARÇO'},
           {'ano': '2021', 'produto': 'ABACAXI', 'mes': 'MARÇO'}]
        lista_produto_ano_mes = Utils.create_list_product_year_month(anos=anos, lista_produtos=lista_produtos,
                                                                     lista_para_meses=lista_para_meses)
        assert lista_produto_ano_mes.__eq__(lista_produto_ano_mesref)

    def test_getlist_urls_cities(self):
        lista_de_meses = ['MAR%C3%87O', 'MAR%C3%87O']
        lista_de_produtos = ['ABACAXI', 'ABACAXI']
        lista_de_anos = ['2022', '2021']
        urls_municipiosref= ['https://pentahoportaldeinformacoes.conab.gov.br/pentaho/plugin/cda/api/doQuery?paramempreendimento=%5BTipo+Empreendimento%5D.%5BTODOS%5D&paramproduto=%5BProduto%5D.%5BABACAXI%5D&paramsafra=%5BTipo+Safra%5D.%5BTODAS%5D&paramano=%5BAno%5D.%5B2022%5D&parammes=%5BMes%5D.%5BMAR%C3%87O%5D&paramclassificacao=%5BProduto+Classificacao%5D.%5BTODAS%5D&path=%2Fhome%2FSIAGRO%2FCustoProducao.cda&dataAccessId=custoVariavelMunicipioProdutividade&outputIndexId=1&pageSize=0&pageStart=0&sortBy=&paramsearchBox=',
                              'https://pentahoportaldeinformacoes.conab.gov.br/pentaho/plugin/cda/api/doQuery?paramempreendimento=%5BTipo+Empreendimento%5D.%5BTODOS%5D&paramproduto=%5BProduto%5D.%5BABACAXI%5D&paramsafra=%5BTipo+Safra%5D.%5BTODAS%5D&paramano=%5BAno%5D.%5B2021%5D&parammes=%5BMes%5D.%5BMAR%C3%87O%5D&paramclassificacao=%5BProduto+Classificacao%5D.%5BTODAS%5D&path=%2Fhome%2FSIAGRO%2FCustoProducao.cda&dataAccessId=custoVariavelMunicipioProdutividade&outputIndexId=1&pageSize=0&pageStart=0&sortBy=&paramsearchBox=']
        urls_municipios = Utils.getlist_urls_cities(lista_de_produtos=lista_de_produtos,
                                                    lista_de_anos=lista_de_anos, lista_de_meses=lista_de_meses)
        assert urls_municipios.__eq__(urls_municipiosref)

    def test_create_cities_list(self):
        lista_de_municipiosref = [['ARAPIRACA-AL', 'CONCEIÇÃO DO ARAGUAIA-PA', 'SANTA RITA-PB'],
                                  ['CONCEIÇÃO DO ARAGUAIA-PA', 'SANTA RITA-PB']]
        citieslist = [[['ARAPIRACA-AL', 1.52, 32000],
                      ['CONCEIÇÃO DO ARAGUAIA-PA', 570.92, 27500],
                      ['SANTA RITA-PB', 961.31, 44]],
                     [['CONCEIÇÃO DO ARAGUAIA-PA', 513.52, 27500], ['SANTA RITA-PB', 706.97, 44]]]
        lista_de_municipios = Utils.create_cities_list(citieslist=citieslist)
        assert  lista_de_municipios.__eq__(lista_de_municipiosref)

    def test_createproduct_year_month_city_list(self):
        lista_produto_ano_mes_municipioref = [{'ano': '2022',
                                              'produto': 'ABACAXI',
                                              'mes': 'MAR%C3%87O',
                                              'municipio': 'ARAPIRACA-AL'},
                                             {'ano': '2022',
                                              'produto': 'ABACAXI',
                                              'mes': 'MAR%C3%87O',
                                              'municipio': 'CONCEIÇÃO DO ARAGUAIA-PA'},
                                             {'ano': '2022',
                                              'produto': 'ABACAXI',
                                              'mes': 'MAR%C3%87O',
                                              'municipio': 'SANTA RITA-PB'},
                                             {'ano': '2021',
                                              'produto': 'ABACAXI',
                                              'mes': 'MAR%C3%87O',
                                              'municipio': 'CONCEIÇÃO DO ARAGUAIA-PA'},
                                             {'ano': '2021',
                                              'produto': 'ABACAXI',
                                              'mes': 'MAR%C3%87O',
                                              'municipio': 'SANTA RITA-PB'}]
        lista_de_meses = ['MAR%C3%87O', 'MAR%C3%87O']
        lista_de_produtos = ['ABACAXI', 'ABACAXI']
        lista_de_anos = ['2022', '2021']
        lista_de_municipios = [['ARAPIRACA-AL', 'CONCEIÇÃO DO ARAGUAIA-PA', 'SANTA RITA-PB'],
                                  ['CONCEIÇÃO DO ARAGUAIA-PA', 'SANTA RITA-PB']]
        lista_produto_ano_mes_municipio = Utils.createproduct_year_month_city_list(lista_de_anos=lista_de_anos,
                                                                                   lista_de_produtos=lista_de_produtos,
                                                                                   lista_de_meses=lista_de_meses,
                                                                                  lista_de_municipios=lista_de_municipios)
        assert lista_produto_ano_mes_municipio.__eq__(lista_produto_ano_mes_municipioref)

    def test_get_urls_to_ingest(self):
        urlsref = ['https://pentahoportaldeinformacoes.conab.gov.br/pentaho/plugin/cda/api/doQuery?paramempreendimento=%5BTipo+Empreendimento%5D.%5BTODOS%5D&paramproduto=%5BProduto%5D.%5BABACAXI%5D&paramsafra=%5BTipo+Safra%5D.%5BTODAS%5D&paramano=%5BAno%5D.%5B2022%5D&parammes=%5BMes%5D.%5BMAR%C3%87O%5D&parammunicipio=ARAPIRACA-AL&paramtipoCusto=CUSTO+VARI%C3%81VEL&path=%2Fhome%2FSIAGRO%2FCustoProducao.cda&dataAccessId=custoDetalhadoMunic&outputIndexId=1&pageSize=0&pageStart=0&sortBy=&paramsearchBox=',
                     'https://pentahoportaldeinformacoes.conab.gov.br/pentaho/plugin/cda/api/doQuery?paramempreendimento=%5BTipo+Empreendimento%5D.%5BTODOS%5D&paramproduto=%5BProduto%5D.%5BABACAXI%5D&paramsafra=%5BTipo+Safra%5D.%5BTODAS%5D&paramano=%5BAno%5D.%5B2022%5D&parammes=%5BMes%5D.%5BMAR%C3%87O%5D&parammunicipio=CONCEI%C3%87%C3%83O+DO+ARAGUAIA-PA&paramtipoCusto=CUSTO+VARI%C3%81VEL&path=%2Fhome%2FSIAGRO%2FCustoProducao.cda&dataAccessId=custoDetalhadoMunic&outputIndexId=1&pageSize=0&pageStart=0&sortBy=&paramsearchBox=',
                     'https://pentahoportaldeinformacoes.conab.gov.br/pentaho/plugin/cda/api/doQuery?paramempreendimento=%5BTipo+Empreendimento%5D.%5BTODOS%5D&paramproduto=%5BProduto%5D.%5BABACAXI%5D&paramsafra=%5BTipo+Safra%5D.%5BTODAS%5D&paramano=%5BAno%5D.%5B2022%5D&parammes=%5BMes%5D.%5BMAR%C3%87O%5D&parammunicipio=SANTA+RITA-PB&paramtipoCusto=CUSTO+VARI%C3%81VEL&path=%2Fhome%2FSIAGRO%2FCustoProducao.cda&dataAccessId=custoDetalhadoMunic&outputIndexId=1&pageSize=0&pageStart=0&sortBy=&paramsearchBox=',
                     'https://pentahoportaldeinformacoes.conab.gov.br/pentaho/plugin/cda/api/doQuery?paramempreendimento=%5BTipo+Empreendimento%5D.%5BTODOS%5D&paramproduto=%5BProduto%5D.%5BABACAXI%5D&paramsafra=%5BTipo+Safra%5D.%5BTODAS%5D&paramano=%5BAno%5D.%5B2021%5D&parammes=%5BMes%5D.%5BMAR%C3%87O%5D&parammunicipio=CONCEI%C3%87%C3%83O+DO+ARAGUAIA-PA&paramtipoCusto=CUSTO+VARI%C3%81VEL&path=%2Fhome%2FSIAGRO%2FCustoProducao.cda&dataAccessId=custoDetalhadoMunic&outputIndexId=1&pageSize=0&pageStart=0&sortBy=&paramsearchBox=',
                     'https://pentahoportaldeinformacoes.conab.gov.br/pentaho/plugin/cda/api/doQuery?paramempreendimento=%5BTipo+Empreendimento%5D.%5BTODOS%5D&paramproduto=%5BProduto%5D.%5BABACAXI%5D&paramsafra=%5BTipo+Safra%5D.%5BTODAS%5D&paramano=%5BAno%5D.%5B2021%5D&parammes=%5BMes%5D.%5BMAR%C3%87O%5D&parammunicipio=SANTA+RITA-PB&paramtipoCusto=CUSTO+VARI%C3%81VEL&path=%2Fhome%2FSIAGRO%2FCustoProducao.cda&dataAccessId=custoDetalhadoMunic&outputIndexId=1&pageSize=0&pageStart=0&sortBy=&paramsearchBox=']
        lista_de_municipios = ['ARAPIRACA-AL',
         'CONCEI%C3%87%C3%83O+DO+ARAGUAIA-PA',
         'SANTA+RITA-PB',
         'CONCEI%C3%87%C3%83O+DO+ARAGUAIA-PA',
         'SANTA+RITA-PB']
        lista_de_anos = ['2022','2022','2022', '2021','2021']
        lista_de_produtos = ['ABACAXI', 'ABACAXI','ABACAXI', 'ABACAXI', 'ABACAXI']
        lista_de_meses = ['MAR%C3%87O', 'MAR%C3%87O', 'MAR%C3%87O', 'MAR%C3%87O', 'MAR%C3%87O']
        urls = Utils.get_urls_to_ingest(lista_de_produtos=lista_de_produtos, lista_de_anos=lista_de_anos,
                                        lista_de_meses=lista_de_meses, lista_de_municipios=lista_de_municipios)
        assert urls.__eq__(urlsref)


    def test_get_df_from_url_data(self):
        data = [{'ano': '2022',
                'produto': 'ABACAXI',
                'mes': 'MAR%C3%87O',
                'municipio': 'ARAPIRACA-AL'}]
        dfref = pd.DataFrame(data)
        with open(filename, "r", encoding='utf-8') as arquivo:
            df = arquivo.read()
        assert df.__eq__(dfref)

    def test_write_file_container(self):

        pathlistsref = ['src/files/raw/conab_custovariavel/2021/01/conab_custovariavel_2021_01.csv']

        with open(filename, "r", encoding='utf-8') as arquivo:
            pathlists = arquivo.read()
        assert pathlists.__eq__(pathlistsref)

    def test_month_numeric_format(self):
        month = {'JANEIRO': '01'}
        monthteste = 'JANEIRO'
        monthnumberref = month['JANEIRO']
        monthnumeric = Utils.month_numeric_format(monthteste)
        assert monthnumeric.__eq__(monthnumberref)
