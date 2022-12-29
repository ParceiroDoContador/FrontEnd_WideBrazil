import boto3
import requests
import json
from datetime import datetime, timedelta, date
import unidecode
import shutil
import base64
import random
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

#=================== Verificação de Liberão ========================#
liberacao = requests.get("https://gliciojunior.notion.site/WIDE-5ed9ee76906a444187fccaaba35702de")
print(f"liberacao: {liberacao}")
if str(liberacao) == "<Response [200]>":
    #======================= Categorias ==============================#
    categoria_receber_salario = "1.01.97"
    categoria_receber_comissao = "1.01.02"
    categoria_receber_dsr = "1.01.03"
    categoria_receber_alimentacao = "1.02.01"
    categoria_receber_reembolso_despesas = "1.04.02"
    categoria_receber_reembolso_saude = "2.01.01"
    categoria_receber_inss = "1.01.96"
    categoria_receber_adiantamento = "1.03.03"
    categoria_receber_irrf = ""
    categoria_receber_previdencia = "1.03.26"
    categoria_receber_inss_empresa = "1.01.99"
    categoria_receber_fgts = "1.01.98"
    categoria_receber_liquido = "1.04.03"
    categoria_receber_ferias = "1.01.94"
    categoria_receber_seguro = "1.04.06"
    categoria_receber_decimo = "1.01.90"
    categoria_receber_flash = "1.01.91"

    categoria_invoice = "1.01.89"

    app_key = '3068480598183'
    app_secret = '91ed53d6746eb516fd6239186c82ad65'
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
                nome_fantasia = cliente["nome_fantasia"]
                razao_social = unidecode.unidecode(razao_social).upper()
                nome_fantasia = unidecode.unidecode(nome_fantasia).upper()  
                print(f'nome: {nome} - razao_social: {razao_social} - nome_fantasia: {nome_fantasia}')              
                if razao_social == nome or nome_fantasia == nome:
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
        #cnv.drawString(30, 500, "Security Deposit")
        cnv.setFont("Helvetica", 10)
        cnv.drawString(440, 500, f' {rate_dados}')
        cnv.drawString(505, 500, f' {amount_dados}')
        '''cnv.drawString(120, 490, f'Security Deposit EOR - {nome} -')
        cnv.drawString(120, 480, f'This amount will be refunded in full to the CONTRACTING PARTY ')
        cnv.drawString(120, 470, f'at the end of the contract or used for employee dismissal expenses')
        cnv.drawString(120, 460, f'(1time the total monthly cost of the employee payroll).')'''
        x = 120
        y = 480        
        posicao = 479        
        for chave in description.keys():
            print(f'description[chave]: {description[chave]}')
            if description[chave] != "":
                cnv.drawString(x, y, f'{chave}:........................................................................................................')   
                cnv.setFillColorRGB(1, 225, 225)   
                cnv.rect(425, posicao, 310, 10, fill=1, stroke=0)            
                cnv.setFillColorRGB(0, 0, 0)      
                cnv.drawString(425, y, f'R$ {description[chave]}')
                y -= 10
                posicao -= 10
        
        cnv.setFont("Helvetica-Bold", 10)

        #============================= Baixo ===================================#
        cnv.drawString(30, 295, "...............................................................................................................................................................................................")
        cnv.setFont("Helvetica", 8)
        cnv.drawString(30, 280, "Payable to: WIDE BRAZIL PEOPLE RECR ESP E SERV")
        cnv.setFont("Helvetica", 10)
        cnv.drawString(310, 280, "BALANCE DUE")
        cnv.setFont("Helvetica-Bold", 17)
        cnv.drawString(400, 278, f"       USD {balance_due}")
        cnv.setFont("Helvetica", 8)
        cnv.drawString(30, 270, "CORPORATIVOS LTDA ")
        cnv.drawString(30, 260, "Intermediary Institution (or Correspondent Bank, Field 56)")
        cnv.drawString(30, 250, "SWIFT Code: CITIUS33 ")
        cnv.drawString(30, 240, "Bank Name: CITI, NEW YORK - Bank Country: UNITED STATES ")
        cnv.drawString(30, 230, "Beneficiary Bank (Field 57):")
        cnv.drawString(30, 220, "SWIFT Code: BPABBRRJ")
        cnv.drawString(30, 210, "BTG Account with CITI, NEW YORK: 36317173")
        cnv.drawString(30, 200, "Bank Name: BANCO BTG PACTUAL S.A.")
        cnv.drawString(30, 190, "Bank Address: PRAIA DE BOTAFOGO, 501, RIO DE JANEIRO")
        cnv.drawString(30, 180, "Bank Country: BRAZIL ")
        cnv.drawString(30, 170, "Beneficiary Customer (Field 59):")
        cnv.drawString(30, 160, "Beneficiary IBAN: BR2930306294000010002827654C1")
        cnv.drawString(30, 150, "Beneficiary Name: WIDE BRAZIL PEOPLE RECRUTAMENTO")
        cnv.drawString(30, 140, "ESPECIALIZADO E SERVICOS CORPORATIVOS LTDA")
        cnv.drawString(30, 130, "Beneficiary Address: Commercial - AL RIO NEGRO, 1030 -")
        cnv.drawString(30, 120, "ALPHAVILLE CENTRO -")
        cnv.drawString(30, 110, "BARUERÍ - SÃO PAULO - 06454000")
        cnv.drawString(30, 100, "Beneficiary Country: BRAZIL")
        cnv.drawString(30, 90, "Remittance Information (Field 70):")
        cnv.drawString(30, 80, "If possible, include invoice number on field 70")
        cnv.drawString(205, 30, "Please let us know if you have any issues with the payment.")
        cnv.drawString(220, 15, "As always, thank you very much for your business.")
        cnv.save()
    def pegar_valor_conta_receber(codigo_cliente_omie, description):
        pagina = 1
        total_de_paginas = 1
        valor_total = 0
        while pagina <= total_de_paginas:
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
                    valor_documento = (f'{valor_documento:,.2f}')
                    valor_documento = valor_documento.replace(",", "_")
                    valor_documento = valor_documento.replace(".", ",")
                    valor_documento = valor_documento.replace("_", ".")
                    if codigo_categoria == categoria_receber_salario:
                        description["Salário"] = valor_documento
                    if codigo_categoria == categoria_receber_comissao:
                        description["Comissão"] = valor_documento
                    if codigo_categoria == categoria_receber_dsr:
                        description["D.S.R. Sobre Comissão"] = valor_documento
                    if codigo_categoria == categoria_receber_alimentacao:
                        description["Vale Refeicao Alimentacao"] = valor_documento
                    if codigo_categoria == categoria_receber_reembolso_despesas:
                        description["Reembolso de despesas"] = valor_documento
                    if codigo_categoria == categoria_receber_reembolso_saude:
                        description["Reembolso Seg. Saúde"] = valor_documento
                    if codigo_categoria == categoria_receber_previdencia:
                        description["Previdência Privada"] = valor_documento
                    if codigo_categoria == categoria_receber_inss_empresa:
                        description["Base INSS Empresa"] = valor_documento
                    if codigo_categoria == categoria_receber_fgts:
                        description["Base F.G.T.S"] = valor_documento
                    if codigo_categoria == categoria_receber_flash:
                        description["Flash"] = valor_documento
                    if codigo_categoria == categoria_receber_ferias:
                        description["Férias"] = valor_documento
                    if codigo_categoria == categoria_receber_decimo:
                        description["Décimo Terceiro"] = valor_documento
                    if codigo_categoria == categoria_receber_seguro:
                        description["Seguro"] = valor_documento
                    if codigo_categoria == categoria_receber_liquido:
                        description["Líquído"] = valor_documento
                    if codigo_categoria == categoria_receber_adiantamento:
                        description["Adiantamento"] = valor_documento
            pagina += 1
        return valor_total, description
    def pegar_data_vencimento():
        data_atual = date.today()
        data_vencimento = data_atual + timedelta(days=30)
        data_atual = data_atual.strftime("%d/%m/%Y")
        data_vencimento = data_vencimento.strftime("%d/%m/%Y")
        return data_vencimento
    def incluir_conta_receber_codigo(codigo_cliente_omie, data_vencimento, valor_documento, codigo_categoria):
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
        codigo_lancamento_omie = response["codigo_lancamento_omie"]
        return codigo_lancamento_omie
    def anexar_invoice(nId, cArquivo):
        cMd5 = "123"
        while True:      
            url = "https://app.omie.com.br/api/v1/geral/anexo/"
            payload = json.dumps({
                                    "call": "IncluirAnexo",
                                    "app_key": app_key,
                                    "app_secret": app_secret,
                                    "param":[
                                                {
                                                    "cTabela": "conta-receber",
                                                    "nId": nId,
                                                    "cNomeArquivo": "invoice.pdf",
                                                    "cTipoArquivo": "",
                                                    "cArquivo": cArquivo,
                                                    "cMd5": cMd5
                                                }
                                            ]
                                })
            headers ={
                        'Content-Type': 'application/json'
                    }
            response = requests.request("POST", url, headers=headers, data=payload)
            response = response.json()
            print(f'IncluirAnexo: {response}')
            try:
                faultstring = response["faultstring"]
                faultstring = faultstring.split(" ")
                faultstring = faultstring[9]
                faultstring = str(faultstring)
                faultstring = faultstring.replace("[", "")
                faultstring = faultstring.replace("]", "")
                cMd5 = faultstring.replace("!", "")
                print(f"cMd5: {cMd5}")      
            except:
                break

    #====================== Recebendo Arquivo S3 ======================#
    s3 = boto3.resource("s3", aws_access_key_id="AKIATX77KZ6NA7RTXMFO", aws_secret_access_key="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")
    bucket = s3.Bucket("parceiro-do-contador-bucket")
    bucket.download_file(Key="arquivos/j_son.json", Filename="j_son.json")
    bucket.download_file(Key="arquivos/logo_fundo_branco.png", Filename="logo_fundo_branco.png")
    with open('j_son.json', 'r') as arquivo:
        j_son = arquivo.read()
    j_son = j_son.replace("'", "\"")
    j_son = json.loads(j_son)
    nome = j_son["nome"]
    print(f'nome: {nome}')
    try:
        nome = nome.encode("windows-1252").decode("utf-8")
    except:
        pass
    cotacao_dolar = j_son["cotacao_dolar"]
    if "," in str(cotacao_dolar):
        cotacao_dolar = cotacao_dolar.replace(",", ".")
    cotacao_dolar = float(cotacao_dolar)

    #codigo_cliente_omie = buscar_codigo_cliente_teste(nome)
    codigo_cliente_omie = buscar_codigo_cliente(nome)
    description = {"Salário": "", "Comissão": "", "D.S.R. Sobre Comissão": "",  "Vale Refeicao Alimentacao": "", "Reembolso de despesas": "", "Reembolso Seg. Saúde": "", "INSS Salário": "",\
    "Adiantamento": "", "IRRF Salário": "", "Previdência Privada": "", "Base INSS Empresa": "", "Base F.G.T.S": "", "Líquído": "", "Férias": "",\
    "Décimo Terceiro": "", "Seguro": "", "Flash": ""}            
    valor_total, description = pegar_valor_conta_receber(codigo_cliente_omie, description)                
    valor_total_dolar = valor_total / cotacao_dolar
    valor_total_dolar = (f'{valor_total_dolar:,.2f}')
    valor_total_dolar = valor_total_dolar.replace(",", "_")
    valor_total_dolar = valor_total_dolar.replace(".", ",")
    valor_total_dolar = valor_total_dolar.replace("_", ".")
    gerar_invoice(valor_total_dolar, nome, description)
    shutil.make_archive('invoice', 'zip', '', 'invoice.pdf')
    with open("invoice.zip", "rb") as arquivo:
        invoice_64 = base64.b64encode(arquivo.read())
    invoice_64 = str(invoice_64)
    invoice_64 = invoice_64[:-1]
    invoice_64 = invoice_64[2:]
    codigo_cliente_omie = buscar_codigo_cliente(nome)
    data_vencimento = pegar_data_vencimento()
    codigo_lancamento_omie = incluir_conta_receber_codigo(codigo_cliente_omie, data_vencimento, valor_total, categoria_invoice)
    anexar_invoice(codigo_lancamento_omie, invoice_64)