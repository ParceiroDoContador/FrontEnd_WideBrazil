import boto3
import pandas as pd
import requests
import json
from datetime import timedelta, date
import random
import os
from reportlab.lib.pagesizes import A4
import unidecode

#=================== Verificação de Liberão ========================#
liberacao = requests.get("https://gliciojunior.notion.site/WIDE-5ed9ee76906a444187fccaaba35702de")
print(f"liberacao: {liberacao}")
if str(liberacao) == "<Response [200]>":

    categoria_pagar_decimo = "2.01.90"
    categoria_receber_decimo = "1.01.90"

    #============================= Funções ============================#
    app_key = '3068480598183'
    app_secret = '91ed53d6746eb516fd6239186c82ad65'
    def incluir_conta_pagar(codigo_cliente_omie, data_vencimento, valor_documento, codigo_categoria):
        randomlist = random.sample(range(1, 12), 8)
        randomlist = str(randomlist)
        aleatorio = randomlist.replace(",","")
        aleatorio = aleatorio.replace(" ","")
        aleatorio = aleatorio.replace("[","")
        codigo_lancamento_integracao = aleatorio.replace("]","")    
        url = "https://app.omie.com.br/api/v1/financas/contapagar/"
        payload = json.dumps({
                                "call": "IncluirContaPagar",
                                "app_key": app_key,
                                "app_secret": app_secret,
                                "param":[
                                            {
                                                "codigo_lancamento_integracao": codigo_lancamento_integracao,
                                                "codigo_cliente_fornecedor": codigo_cliente_omie,
                                                "data_vencimento": data_vencimento,
                                                "valor_documento": valor_documento,
                                                "codigo_categoria": codigo_categoria
                                            }
                                        ]
                            })
        headers ={
                    'Content-Type': 'application/json'
                }
        response = requests.request("POST", url, headers=headers, data=payload)
        response = response.json()
        print(f'IncluirContaPagar: {response}')
    def incluir_conta_receber(codigo_cliente_omie, data_vencimento, valor_documento, codigo_categoria):
        randomlist = random.sample(range(1, 12), 8)
        randomlist = str(randomlist)
        aleatorio = randomlist.replace(",","")
        aleatorio = aleatorio.replace(" ","")
        aleatorio = aleatorio.replace("[","")
        codigo_lancamento_integracao = aleatorio.replace("]","")    
        url = "https://app.omie.com.br/api/v1/financas/contareceber/"
        payload = json.dumps({
                                "call": "IncluirContaReceber",
                                "app_key": app_key,
                                "app_secret": app_secret,
                                "param":[
                                            {
                                                "codigo_lancamento_integracao": codigo_lancamento_integracao,
                                                "codigo_cliente_fornecedor": codigo_cliente_omie,
                                                "data_vencimento": data_vencimento,
                                                "valor_documento": valor_documento,
                                                "codigo_categoria": codigo_categoria,
                                                "id_conta_corrente": "7311700205"
                                            }
                                        ]
                            })
        headers ={
                    'Content-Type': 'application/json'
                }
        response = requests.request("POST", url, headers=headers, data=payload)
        response = response.json()
        print(f'IncluirContaReceber: {response}')
    def buscar_codigo_cliente_teste(nome):
        nome = unidecode.unidecode(nome).upper()
        pagina = 1
        total_de_paginas = 1
        while pagina <= total_de_paginas:
            url = "https://app.omie.com.br/api/v1/geral/clientes/"
            payload = json.dumps({
                                    "call": "ListarClientes",
                                    "app_key": app_key,
                                    "app_secret": app_secret,
                                    "param":[
                                                {
                                                    "pagina": pagina,
                                                    "registros_por_pagina": 500,
                                                    "apenas_importado_api": "N"
                                                }
                                            ]
                                })
            headers ={
                        'Content-Type': 'application/json'
                    }
            response = requests.request("POST", url, headers=headers, data=payload)
            response = response.json()
            pagina = response["pagina"]
            total_de_paginas = response["total_de_paginas"]
            clientes_cadastro = response["clientes_cadastro"]
            for cliente in clientes_cadastro:
                try:
                    contato = cliente["contato"]
                    contato = unidecode.unidecode(contato).upper()
                    if contato == nome:
                        codigo_cliente_omie = cliente["codigo_cliente_omie"]
                        break
                except:
                    pass        
            pagina += 1
        return codigo_cliente_omie
    def buscar_codigo_cliente(nome):
        nome = unidecode.unidecode(nome).upper()
        pagina = 1
        total_de_paginas = 1
        while pagina <= total_de_paginas:
            url = "https://app.omie.com.br/api/v1/geral/clientes/"
            payload = json.dumps({
                                    "call": "ListarClientes",
                                    "app_key": app_key,
                                    "app_secret": app_secret,
                                    "param":[
                                                {
                                                    "pagina": pagina,
                                                    "registros_por_pagina": 500,
                                                    "apenas_importado_api": "N"
                                                }
                                            ]
                                })
            headers ={
                        'Content-Type': 'application/json'
                    }
            response = requests.request("POST", url, headers=headers, data=payload)
            response = response.json()
            pagina = response["pagina"]
            total_de_paginas = response["total_de_paginas"]
            clientes_cadastro = response["clientes_cadastro"]
            for cliente in clientes_cadastro:  
                razao_social = cliente["razao_social"]
                razao_social = unidecode.unidecode(razao_social).upper()
                if razao_social == nome:
                    codigo_cliente_omie = cliente["codigo_cliente_omie"]
                    break
            pagina += 1
        return codigo_cliente_omie
    def pegar_data_vencimento():
        data_atual = date.today()
        data_vencimento = data_atual + timedelta(days=30)
        data_atual = data_atual.strftime("%d/%m/%Y")
        data_vencimento = data_vencimento.strftime("%d/%m/%Y")
        return data_vencimento

    #================= Data vencimento =================#
    data_atual = date.today()
    data_vencimento = data_atual + timedelta(days=30)
    data_atual = data_atual.strftime("%d/%m/%Y")
    data_vencimento = data_vencimento.strftime("%d/%m/%Y")

    #====================== Recebendo Arquivo S3 ======================#
    s3 = boto3.resource("s3", aws_access_key_id="AKIATX77KZ6NA7RTXMFO", aws_secret_access_key="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")
    bucket = s3.Bucket("parceiro-do-contador-bucket")
    bucket.download_file(Key="import2/décimo.pdf", Filename="planilha_decimo_terceiro")
    os.rename("planilha_decimo_terceiro", "planilha_decimo_terceiro.xls")

    #================ Extraindo dados da planilha ===================#
    data_vencimento = pegar_data_vencimento()
    planilha_decimo_terceiro = pd.read_excel("planilha_decimo_terceiro.xls")
    linha_planilha = 3
    total_linhas = planilha_decimo_terceiro.shape[0]
    while linha_planilha < total_linhas:
        dados = planilha_decimo_terceiro.loc[linha_planilha]
        nome = dados[1]        
        if str(nome) == "nan":
            break
        decimo_terceiro = dados[12]
        ##########################
        #nome = "Paulo"
        ##########################
        #codigo_cliente_omie = buscar_codigo_cliente_teste(nome)
        codigo_cliente_omie = buscar_codigo_cliente(nome)
        decimo_terceiro = dados[12]
        nome = dados[1]
        print(f"nome: {nome} - codigo_cliente_omie: {codigo_cliente_omie} - decimo_terceiro: {decimo_terceiro}")
        incluir_conta_receber(codigo_cliente_omie, data_vencimento, decimo_terceiro, categoria_receber_decimo) 
        incluir_conta_pagar(codigo_cliente_omie, data_vencimento, decimo_terceiro, categoria_pagar_decimo) 
        linha_planilha += 1