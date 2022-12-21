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
liberacao = requests.get("https://gliciojunior.notion.site/WIDE-BRAZIL-PEOPLE-RECRUTAMENTO-ESPECIALIZADO-E-SERVICOS-CORPORATIVOS-LTDA-e13c02ae0f0f4af3b5af1a1a72c69aff")
print(f"liberacao: {liberacao}")
if str(liberacao) == "<Response [200]>":
    
    #======================= Categorias ==============================#
    categoria_salario = "1.01.01"
    categoria_comissao = "1.01.02"
    categoria_dsr = "1.01.03"
    categoria_alimentacao = "1.02.01"
    categoria_reembolso_despesas = "1.02.02"
    categoria_reembolso_saude = "1.03.01"
    categoria_inss = "1.03.02"
    categoria_adiantamento = "1.03.03"
    categoria_irrf = ""
    categoria_previdencia = "1.03.26"
    categoria_inss_empresa = "1.04.01"
    categoria_fgts = "2.01.02"
    categoria_liquido = "1.04.03"

    #============================= Funções ============================#
    app_key = '3047558285772'
    app_secret = '5442899c8726947cc0c20ab1697d8286'

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
            app_key = '3068480598183'
            app_secret = '91ed53d6746eb516fd6239186c82ad65'
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
        print(f"\n\nlancamento: {lancamento} - provento: {provento} - desconto: {desconto} - base: {base} - liquido: {liquido}")
        #nome = "Paulo"
        if nome != nome_anterior:
            codigo_cliente_omie = buscar_codigo_cliente(nome)

        if lancamento == "Salário" or lancamento == "Saldo de Salário":
            incluir_conta_receber(codigo_cliente_omie, data_vencimento, provento, categoria_salario)
            print(provento)

        if lancamento == "Comissão":
            incluir_conta_pagar(codigo_cliente_omie, data_vencimento, provento, categoria_comissao)
            incluir_conta_receber(codigo_cliente_omie, data_vencimento, provento, categoria_comissao)
            print(provento)

        if lancamento == "D.S.R. Sobre Comissão":
            incluir_conta_pagar(codigo_cliente_omie, data_vencimento, provento, categoria_dsr)
            incluir_conta_receber(codigo_cliente_omie, data_vencimento, provento, categoria_dsr)
            print(provento)

        if lancamento == "Vale Refeicao Alimentacao":
            incluir_conta_pagar(codigo_cliente_omie, data_vencimento, provento, categoria_alimentacao)
            incluir_conta_receber(codigo_cliente_omie, data_vencimento, provento, categoria_alimentacao)
            print(provento)

        if lancamento == "Reembolso de despesas":
            incluir_conta_pagar(codigo_cliente_omie, data_vencimento, provento, categoria_reembolso_despesas)
            incluir_conta_receber(codigo_cliente_omie, data_vencimento, provento, categoria_reembolso_despesas)
            print(provento)

        if lancamento == "Reembolso Seg. Saúde":
            incluir_conta_pagar(codigo_cliente_omie, data_vencimento, provento, categoria_reembolso_saude)
            incluir_conta_receber(codigo_cliente_omie, data_vencimento, provento, categoria_reembolso_saude)
            print(provento)

        if lancamento == "INSS Sobre Salário":
            incluir_conta_pagar(codigo_cliente_omie, data_vencimento, desconto, categoria_inss)
            print(desconto)

        if lancamento == "Adiantamento Anterior":
            incluir_conta_pagar(codigo_cliente_omie, data_vencimento, desconto, categoria_adiantamento)
            incluir_conta_receber(codigo_cliente_omie, data_vencimento, desconto, categoria_adiantamento)
            print(desconto)

        if lancamento == "IRRF Sobre Salário":
            incluir_conta_pagar(codigo_cliente_omie, data_vencimento, desconto, categoria_irrf)
            print(desconto)

        if lancamento == "Previdência Privada":
            incluir_conta_pagar(codigo_cliente_omie, data_vencimento, desconto, categoria_previdencia)
            incluir_conta_receber(codigo_cliente_omie, data_vencimento, desconto, categoria_previdencia)
            print(desconto)

        if lancamento == "Base INSS Empresa":        
            base = base * 0.288
            base = f"{base:.2f}"
            incluir_conta_pagar(codigo_cliente_omie, data_vencimento, base, categoria_inss_empresa)
            incluir_conta_receber(codigo_cliente_omie, data_vencimento, base, categoria_inss_empresa)
            print(base)      

        if lancamento == "Base F.G.T.S.":
            incluir_conta_pagar(codigo_cliente_omie, data_vencimento, base, categoria_fgts)
            incluir_conta_receber(codigo_cliente_omie, data_vencimento, base, categoria_fgts)
            print(base)

        if lancamento == "Líquído":
            incluir_conta_pagar(codigo_cliente_omie, data_vencimento, liquido, categoria_liquido)
            print(liquido) 
        
        nome_anterior = nome
        linha_planilha += 1