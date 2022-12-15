import os
import boto3
import requests
import json
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import time
import unidecode

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
def gerar_invoice(valor_total_dolar, nome, description):    
    data_inicio = datetime.now().strftime('%d/%m/%Y')
    data_final = "Data Final"
    balance_due = valor_total_dolar
    amount_dados = valor_total_dolar
    rate_dados = valor_total_dolar
    balance_due = str(balance_due)
    amount_dados = str(amount_dados)
    rate_dados = str(rate_dados)

    cnv = canvas.Canvas("invoice.pdf", pagesize=A4)

    #========================= SUPERIOR ============================#
    cnv.setFont("Helvetica-Bold", 10)
    cnv.drawString(30, 800, "WIDE BRAZIL PEOPLE RECRUT. ESP. E")
    cnv.drawString(30, 785, "SERV. CORP. LTDA")
    cnv.setFont("Helvetica", 10)
    cnv.drawString(30, 770, "1030 Alameda Rio Negro - Escritório 206")
    cnv.drawString(30, 755, "Barueri, SP 06454-000 BR")
    cnv.drawString(30, 740, "info@widebrazil.com")
    cnv.drawString(30, 725, "CNPJ TAX ID 41450051000100")
    cnv.setFont("Helvetica", 20)
    cnv.setFillColorRGB(0.2, 0.4, 0.33)
    cnv.drawString(30, 705, "INVOICE")
    cnv.setFont("Helvetica-Bold", 10)
    cnv.setFillColorRGB(0, 0, 0)
    cnv.drawString(30, 675, "BILL TO")
    cnv.drawString(355, 675, "   INVOICE NO.")
    cnv.setFont("Helvetica", 10)
    cnv.drawString(430, 675, "     WORKA_secdep_IM")
    cnv.drawString(30, 660, "WORCA PTE. LTD.")
    cnv.setFont("Helvetica-Bold", 10)
    cnv.drawString(390, 660, "   DATE")
    cnv.setFont("Helvetica", 10)
    cnv.drawString(430, 660, f"     {data_inicio}")
    cnv.drawString(30, 645, "Mr. Chia-yu Wu")
    cnv.setFont("Helvetica-Bold", 10)
    cnv.drawString(365, 645, "   DUE DATE ")
    cnv.setFont("Helvetica", 10)
    cnv.drawString(430, 645, f"     {data_final}")
    cnv.drawString(30, 630, "68 Circular Road#02-01 -")
    cnv.drawString(30, 615, "Singapore (049422)")
    cnv.drawImage("logo_fundo_branco.png", 450, 790, width=90, height=30)
    cnv.setFillColorRGB(0.2, 0.4, 0.33)
    cnv.rect(30, 590, 533, 0.2, fill=1, stroke=0)

    #====================== TABELA =================================#
    cnv.setFillColorRGB(0.83, 0.87, 0.82)
    cnv.rect(20, 515, 555, 18, fill=1, stroke=0)
    cnv.setFillColorRGB(0, 0, 0)
    cnv.setFillColorRGB(0.2, 0.4, 0.33)
    cnv.drawString(120, 520, "DESCRIPTION                                                                                            RATE              AMOUNT")
    cnv.setFillColorRGB(0, 0, 0)
    cnv.setFont("Helvetica-Bold", 10)
    cnv.drawString(30, 500, "Security Deposit")
    cnv.setFont("Helvetica", 10)
    cnv.drawString(440, 500, f' {rate_dados}')
    cnv.drawString(505, 500, f' {amount_dados}')
    cnv.drawString(120, 490, f'Security Deposit EOR - {nome} -')
    cnv.drawString(120, 480, f'This amount will be refunded in full to the CONTRACTING PARTY ')
    cnv.drawString(120, 470, f'at the end of the contract or used for employee dismissal expenses')
    cnv.drawString(120, 460, f'(1time the total monthly cost of the employee payroll).')
    cnv.drawString(120, 445, f'Salário:............................................................................R$ {description["ferias"]}')
    cnv.drawString(120, 435, f'Comissão:.......................................................................R$ {description["decimo_terceiro"]}')
    cnv.drawString(120, 425, f'D.S.R. Sobre Comissão:.................................................R$ {description["seguro"]}')
    cnv.drawString(120, 415, f'Vale Refeicao Alimentacao:............................................R$ {description["flash"]}')
    cnv.setFont("Helvetica-Bold", 10)
    cnv.drawString(30, 500, "Security Deposit")

    #============================= Baixo ===================================#
    cnv.drawString(30, 320, "...............................................................................................................................................................................................")
    cnv.setFont("Helvetica", 8)
    cnv.drawString(30, 290, "Payable to: WIDE BRAZIL PEOPLE RECR ESP E SERV")
    cnv.setFont("Helvetica", 10)
    cnv.drawString(310, 290, "BALANCE DUE")
    cnv.setFont("Helvetica-Bold", 17)
    cnv.drawString(400, 288, f"       USD {balance_due}")
    cnv.setFont("Helvetica", 8)
    cnv.drawString(30, 280, "CORPORATIVOS LTDA ")
    cnv.drawString(30, 270, "Intermediary Institution (or Correspondent Bank, Field 56)")
    cnv.drawString(30, 260, "SWIFT Code: CITIUS33 ")
    cnv.drawString(30, 250, "Bank Name: CITI, NEW YORK - Bank Country: UNITED STATES ")
    cnv.drawString(30, 240, "Beneficiary Bank (Field 57):")
    cnv.drawString(30, 230, "SWIFT Code: BPABBRRJ")
    cnv.drawString(30, 220, "BTG Account with CITI, NEW YORK: 36317173")
    cnv.drawString(30, 210, "Bank Name: BANCO BTG PACTUAL S.A.")
    cnv.drawString(30, 200, "Bank Address: PRAIA DE BOTAFOGO, 501, RIO DE JANEIRO")
    cnv.drawString(30, 190, "Bank Country: BRAZIL ")
    cnv.drawString(30, 180, "Beneficiary Customer (Field 59):")
    cnv.drawString(30, 170, "Beneficiary IBAN: BR2930306294000010002827654C1")
    cnv.drawString(30, 160, "Beneficiary Name: WIDE BRAZIL PEOPLE RECRUTAMENTO")
    cnv.drawString(30, 150, "ESPECIALIZADO E SERVICOS CORPORATIVOS LTDA")
    cnv.drawString(30, 140, "Beneficiary Address: Commercial - AL RIO NEGRO, 1030 -")
    cnv.drawString(30, 130, "ALPHAVILLE CENTRO -")
    cnv.drawString(30, 120, "BARUERÍ - SÃO PAULO - 06454000")
    cnv.drawString(30, 110, "Beneficiary Country: BRAZIL")
    cnv.drawString(30, 100, "Remittance Information (Field 70):")
    cnv.drawString(30, 90, "If possible, include invoice number on field 70")
    cnv.drawString(205, 40, "Please let us know if you have any issues with the payment.")
    cnv.drawString(220, 25, "As always, thank you very much for your business.")
    cnv.save()
def pegar_valor_conta_receber(codigo_cliente_omie, description):
    pagina = 1
    total_de_paginas = 1
    valor_total = 0
    while pagina <= total_de_paginas:
        app_key = '3047558285772'
        app_secret = '5442899c8726947cc0c20ab1697d8286'
        url = "https://app.omie.com.br/api/v1/financas/contareceber/"
        payload = json.dumps({
                                "call": "ListarContasReceber",
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
        conta_receber_cadastro = response["conta_receber_cadastro"]
        for conta_receber in conta_receber_cadastro:
            codigo_cliente_fornecedor = conta_receber["codigo_cliente_fornecedor"]
            status_titulo = conta_receber["status_titulo"]
            if codigo_cliente_fornecedor == codigo_cliente_omie and status_titulo != "RECEBIDO":
                valor_total += float(conta_receber["valor_documento"])
                categorias = conta_receber["categorias"]
                categorias = categorias[0]
                codigo_categoria = categorias["codigo_categoria"]
                valor_documento = conta_receber["valor_documento"]
                if codigo_categoria == "1.01.03":
                    description["ferias"] = valor_documento
                if codigo_categoria == "1.01.03":
                    description["decimo_terceiro"] = valor_documento
                if codigo_categoria == "1.01.03":
                    description["seguro"] = valor_documento
                if codigo_categoria == "1.01.03":
                    description["flash"] = valor_documento
        pagina += 1
    return valor_total, description

#====================== Recebendo Arquivo S3 ======================#
s3 = boto3.resource("s3", aws_access_key_id="AKIATX77KZ6NA7RTXMFO", aws_secret_access_key="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")
bucket = s3.Bucket("parceiro-do-contador-bucket")
bucket.download_file(Key="arquivos/j_son.json", Filename="j_son.json")
bucket.download_file(Key="arquivos/logo_fundo_branco.png", Filename="logo_fundo_branco.png")

with open('j_son.json', 'r') as arquivo:
    j_son = arquivo.read()
j_son = j_son.replace("'", "\"")
j_son = json.loads(j_son)
nome = j_son["nome"].upper()
cotacao_dolar = j_son["cotacao_dolar"]
cotacao_dolar = float(cotacao_dolar)
print(f"nome: {nome} - cotacao_dolar: {cotacao_dolar}")
codigo_cliente_omie = buscar_codigo_cliente_teste(nome)
description = {"ferias": "", "decimo_terceiro": "", "seguro": "", "flash": ""}
valor_total, description = pegar_valor_conta_receber(codigo_cliente_omie, description)
valor_total_dolar = valor_total / cotacao_dolar
valor_total_dolar = (f'{valor_total_dolar:,.2f}')
valor_total_dolar = valor_total_dolar.replace(",", "_")
valor_total_dolar = valor_total_dolar.replace(".", ",")
valor_total_dolar = valor_total_dolar.replace("_", ".")
gerar_invoice(valor_total_dolar, nome, description)
bucket.upload_file(Key="arquivos/invoice.pdf", Filename="invoice.pdf")