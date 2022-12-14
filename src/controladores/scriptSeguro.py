import boto3
import pandas as pd
import requests
import json
from datetime import timedelta, date
import random
from reportlab.lib.pagesizes import A4
import unidecode
import os

codigo_categoria_seguro = "1.01.03"

#============================= Funções ============================#
def incluir_conta_pagar(codigo_cliente_omie, data_vencimento, valor_documento, codigo_categoria):
    randomlist = random.sample(range(1, 12), 8)
    randomlist = str(randomlist)
    aleatorio = randomlist.replace(",","")
    aleatorio = aleatorio.replace(" ","")
    aleatorio = aleatorio.replace("[","")
    codigo_lancamento_integracao = aleatorio.replace("]","")

    app_key = '3047558285772'
    app_secret = '5442899c8726947cc0c20ab1697d8286'
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

    app_key = '3047558285772'
    app_secret = '5442899c8726947cc0c20ab1697d8286'
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
                                            "id_conta_corrente": "5802271497"
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
        app_key = '3047558285772'
        app_secret = '5442899c8726947cc0c20ab1697d8286'
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
        app_key = '3047558285772'
        app_secret = '5442899c8726947cc0c20ab1697d8286'
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

#================= Data vencimento =================#
data_atual = date.today()
data_vencimento = data_atual + timedelta(days=30)
data_atual = data_atual.strftime("%d/%m/%Y")
data_vencimento = data_vencimento.strftime("%d/%m/%Y")

#====================== Recebendo Arquivo S3 ======================#
s3 = boto3.resource("s3", aws_access_key_id="AKIATX77KZ6NA7RTXMFO", aws_secret_access_key="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")
bucket = s3.Bucket("parceiro-do-contador-bucket")
bucket.download_file(Key="import4/seguro.pdf", Filename="planilha_seguro")

#====================== Lancando Contas ===========================#
os.rename(r'planilha_seguro', r'planilha_seguro.xls')
planilha_seguro = pd.read_excel(r"planilha_seguro.xls")
linha_planilha = 1
total_linhas = planilha_seguro.shape[0]
while linha_planilha < total_linhas:
    dados = planilha_seguro.loc[linha_planilha]
    nome = dados[13]
    if str(nome) == "nan":
        break
    ##########################
    nome = "Paulo"
    ##########################
    #codigo_cliente_omie = buscar_codigo_cliente(nome)
    codigo_cliente_omie = buscar_codigo_cliente_teste(nome)
    premio = dados[18]
    nome = dados[13]
    print(f"nome: {nome} - codigo_cliente_omie: {codigo_cliente_omie} - premio: {premio}")
    incluir_conta_pagar(codigo_cliente_omie, data_vencimento, premio, codigo_categoria=codigo_categoria_seguro)  
    linha_planilha += 1