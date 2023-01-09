import boto3
import pandas as pd
import requests
import json
from datetime import timedelta, date
import random
import os
from reportlab.lib.pagesizes import A4
import unidecode
from variaveis import credentials, categorias_receber_folha, categorias_pagar_folha
from variaveis import conta_corrente
from config import database_infos

app_key = database_infos["app_key"]
app_secret = database_infos["app_secret"]
id_conta_corrente = database_infos["id_conta_corrente"]

#=================== Verificação de Liberão ========================#
liberacao = requests.get("https://gliciojunior.notion.site/WIDE-5ed9ee76906a444187fccaaba35702de")
print(f"liberacao: {liberacao}")
if str(liberacao) == "<Response [200]>":
    
    #======================= Categorias ==============================#
    # RECEBER
    categoria_receber_salario,\
    categoria_receber_comissao,\
    categoria_receber_dsr,\
    categoria_receber_alimentacao,\
    categoria_receber_reembolso_despesas,\
    categoria_receber_reembolso_saude,\
    categoria_receber_inss,\
    categoria_receber_adiantamento,\
    categoria_receber_previdencia,\
    categoria_receber_inss_empresa,\
    categoria_receber_fgts = categorias_receber_folha()
    # PAGAR
    categoria_pagar_liquido,\
    categoria_pagar_irrf,\
    categoria_pagar_fgts,\
    categoria_pagar_inss_empresa,\
    categoria_pagar_reembolso_saude,\
    categoria_pagar_reembolso_despesas,\
    categoria_pagar_inss,\
    categoria_pagar_comissao,\
    categoria_pagar_dsr,\
    categoria_pagar_alimentacao,\
    categoria_pagar_adiantamento,\
    categoria_pagar_previdencia = categorias_pagar_folha()

    #============================= Funções ============================#
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
                                                "id_conta_corrente": id_conta_corrente
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
    bucket.download_file(Key="import5/folha_pagamento.pdf", Filename="planilha_folha_pagamento")

    os.rename('planilha_folha_pagamento', 'planilha_folha_pagamento.xlsx')
    data_vencimento = pegar_data_vencimento()
    planilha_folha_pagamento = pd.read_excel("planilha_folha_pagamento.xlsx", header=None)
    planilha_folha_pagamento = planilha_folha_pagamento.drop(0)
    planilha_folha_pagamento = planilha_folha_pagamento.drop(1)
    total_linhas = planilha_folha_pagamento.shape[0]
    linha_planilha = 3
    nome_anterior = ""
    while linha_planilha < total_linhas:
        dados = planilha_folha_pagamento.loc[linha_planilha]
        nome = dados[1]
        lancamento = dados[2]
        provento = dados[3]
        desconto = dados[4]
        base = dados[5]
        liquido = dados[6]
        print(f"\n\nnome: {nome} - lancamento: {lancamento} - provento: {provento} - desconto: {desconto} - base: {base} - liquido: {liquido}")
        if nome != nome_anterior:
            codigo_cliente_omie = buscar_codigo_cliente(nome)

        if lancamento == "Salário" or lancamento == "Saldo de Salário":
            incluir_conta_receber(codigo_cliente_omie, data_vencimento, provento, categoria_receber_salario)
            print(provento)

        if lancamento == "Comissão":
            incluir_conta_pagar(codigo_cliente_omie, data_vencimento, provento, categoria_receber_comissao)
            incluir_conta_receber(codigo_cliente_omie, data_vencimento, provento, categoria_pagar_comissao)
            print(provento)

        if lancamento == "D.S.R. Sobre Comissão":
            incluir_conta_pagar(codigo_cliente_omie, data_vencimento, provento, categoria_pagar_dsr)
            incluir_conta_receber(codigo_cliente_omie, data_vencimento, provento, categoria_receber_dsr)
            print(provento)

        if lancamento == "Vale Refeicao Alimentacao":
            incluir_conta_pagar(codigo_cliente_omie, data_vencimento, provento, categoria_pagar_alimentacao)
            incluir_conta_receber(codigo_cliente_omie, data_vencimento, provento, categoria_receber_alimentacao)
            print(provento)

        if lancamento == "Reembolso de despesas":
            incluir_conta_pagar(codigo_cliente_omie, data_vencimento, provento, categoria_receber_reembolso_despesas)
            incluir_conta_receber(codigo_cliente_omie, data_vencimento, provento, categoria_pagar_reembolso_despesas)
            print(provento)

        if lancamento == "Reembolso Seg. Saúde":
            incluir_conta_pagar(codigo_cliente_omie, data_vencimento, provento, categoria_pagar_reembolso_saude)
            incluir_conta_receber(codigo_cliente_omie, data_vencimento, provento, categoria_receber_reembolso_saude)
            print(provento)

        if lancamento == "INSS Sobre Salário":
            incluir_conta_pagar(codigo_cliente_omie, data_vencimento, desconto, categoria_pagar_inss)
            print(desconto)

        if lancamento == "Adiantamento Anterior":
            incluir_conta_pagar(codigo_cliente_omie, data_vencimento, desconto, categoria_pagar_adiantamento)
            incluir_conta_receber(codigo_cliente_omie, data_vencimento, desconto, categoria_receber_adiantamento)
            print(desconto)

        if lancamento == "IRRF Sobre Salário":
            incluir_conta_pagar(codigo_cliente_omie, data_vencimento, desconto, categoria_pagar_irrf)
            print(desconto)

        if lancamento == "Previdência Privada":
            incluir_conta_pagar(codigo_cliente_omie, data_vencimento, desconto, categoria_pagar_previdencia)
            incluir_conta_receber(codigo_cliente_omie, data_vencimento, desconto, categoria_receber_previdencia)
            print(desconto)

        if lancamento == "Base INSS Empresa":        
            base = base * 0.288
            base = f"{base:.2f}"
            incluir_conta_pagar(codigo_cliente_omie, data_vencimento, base, categoria_pagar_inss_empresa)
            incluir_conta_receber(codigo_cliente_omie, data_vencimento, base, categoria_receber_inss_empresa)
            print(base)      

        if lancamento == "Base F.G.T.S.":
            incluir_conta_pagar(codigo_cliente_omie, data_vencimento, base, categoria_pagar_fgts)
            incluir_conta_receber(codigo_cliente_omie, data_vencimento, base, categoria_receber_fgts)
            print(base)

        if lancamento == "Líquído":
            incluir_conta_pagar(codigo_cliente_omie, data_vencimento, liquido, categoria_pagar_liquido)
            print(liquido) 
        
        nome_anterior = nome
        linha_planilha += 1