import os
import boto3
import pandas as pd
import requests
import json
from datetime import timedelta, date
import random
from reportlab.lib.pagesizes import A4
import unidecode

#=================== Verificação de Liberão ========================#
liberacao = requests.get("https://gliciojunior.notion.site/WIDE-5ed9ee76906a444187fccaaba35702de")
print(f"liberacao: {liberacao}")
if str(liberacao) == "<Response [200]>":
    
    categoria_receber_flash = "1.01.03"
    categoria_pagar_flash = "2.03.12"

    #============================= Funções ============================#
    app_key = '2892438774225'
    app_secret = '99e922ea95545adfe02a267b7607e37d'
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

    #====================== Recebendo Arquivo S3 ======================#
    s3 = boto3.resource("s3", aws_access_key_id="AKIATX77KZ6NA7RTXMFO", aws_secret_access_key="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")
    bucket = s3.Bucket("parceiro-do-contador-bucket")
    bucket.download_file(Key="import3/flash.pdf", Filename="planilha_flash")

    os.rename(r'planilha_flash', r'planilha_flash.csv')
    planilha_flash = pd.read_csv(r"planilha_flash.csv")
    data_vencimento = pegar_data_vencimento()
    dados = planilha_flash.loc[0]
    linha_planilha = 0
    total_linhas = planilha_flash.shape[0]
    while linha_planilha < total_linhas:
        dados = planilha_flash.loc[linha_planilha]          
        flash = dados[11]
        if str(flash) == "nan":
            break
        #codigo_cliente_omie = buscar_codigo_cliente("teste")
        codigo_cliente_omie = buscar_codigo_cliente("Indústria de Malhas")
        print(f"codigo_cliente_omie: {codigo_cliente_omie} - flash: {flash}")
        incluir_conta_pagar(codigo_cliente_omie, data_vencimento, flash, categoria_pagar_flash)
        incluir_conta_receber(codigo_cliente_omie, data_vencimento, flash, categoria_receber_flash)
        linha_planilha += 1