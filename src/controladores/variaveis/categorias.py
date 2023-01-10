def categorias_decimo_terceiro():
    """Retorna o código categoria, Despesa e Receita do décimo terceiro
    param:  - None
    return: - categoria_pagar_decimo
            - categoria_receber_decimo
    """
    categoria_pagar_decimo = "2.03.05"
    categoria_receber_decimo = "1.01.94"
    return categoria_pagar_decimo, categoria_receber_decimo

def categorias_ferias():
    """Retorna o código categoria, Despesa e Receita de férias
    param:  - None
    return: - categoria_pagar_ferias
            - categoria_receber_ferias"""
    categoria_pagar_ferias = "2.03.03"
    categoria_receber_ferias = "1.01.97"
    return categoria_pagar_ferias, categoria_receber_ferias

def categorias_flash():
    """Retorna o código categoria, Despesa e Receita de vale refeição
    param:  - None
    return: - categoria_receber_flash
            - categoria_pagar_flash"""
    categoria_receber_flash = "1.01.03"
    categoria_pagar_flash = "2.03.12"
    return categoria_receber_flash, categoria_pagar_flash

def categorias_seguro():
    """Retorna o código categoria, Despesa e Receita do seguro
    param:  - None
    return: - categoria_receber_seguro
            - categoria_pagar_seguro"""
    categoria_receber_seguro = "1.01.85"
    categoria_pagar_seguro = "2.03.13"
    return categoria_receber_seguro, categoria_pagar_seguro

def categorias_receber_folha():
    """Retorna o código categoria de receitas da folha de pagamento
    param:  - None
    return: - categoria_receber_salario
            - categoria_receber_comissao
            - categoria_receber_dsr
            - categoria_receber_alimentacao
            - categoria_receber_reembolso_despesas
            - categoria_receber_reembolso_saude
            - categoria_receber_inss
            - categoria_receber_adiantamento
            - categoria_receber_previdencia
            - categoria_receber_inss_empresa
            - categoria_receber_fgts"""

    categoria_receber_salario = "1.01.98"
    categoria_receber_comissao = "1.01.87"
    categoria_receber_dsr = "1.01.95"
    categoria_receber_alimentacao = "1.01.03"
    categoria_receber_reembolso_despesas = "1.04.02"
    categoria_receber_reembolso_saude = "1.01.92"
    categoria_receber_inss = "1.01.91"
    categoria_receber_adiantamento = "1.04.01"    
    categoria_receber_previdencia = "1.01.90"
    categoria_receber_inss_empresa = "1.01.89"
    categoria_receber_fgts = "1.01.88"
    return categoria_receber_salario,\
            categoria_receber_comissao,\
            categoria_receber_dsr,\
            categoria_receber_alimentacao,\
            categoria_receber_reembolso_despesas,\
            categoria_receber_reembolso_saude,\
            categoria_receber_inss,\
            categoria_receber_adiantamento,\
            categoria_receber_previdencia,\
            categoria_receber_inss_empresa,\
            categoria_receber_fgts

def categorias_pagar_folha():
    """Retorna o código categoria de despesas da folha de pagamento
    param:  - None
    return: - categoria_pagar_liquido
            - categoria_pagar_irrf
            - categoria_pagar_fgts
            - categoria_pagar_inss_empresa
            - categoria_pagar_reembolso_saude
            - categoria_pagar_reembolso_despesas
            - categoria_pagar_inss
            - categoria_pagar_comissao
            - categoria_pagar_dsr
            - categoria_pagar_alimentacao
            - categoria_pagar_adiantamento
            - categoria_pagar_previdencia"""

    categoria_pagar_liquido = "2.03.94"
    categoria_pagar_irrf = "2.03.96"
    categoria_pagar_fgts = "2.03.95"
    categoria_pagar_inss_empresa = "2.03.99"
    categoria_pagar_reembolso_saude = "2.03.97"
    categoria_pagar_reembolso_despesas = "2.03.08"
    categoria_pagar_inss = "2.03.06"
    categoria_pagar_comissao = "2.02.01"
    categoria_pagar_dsr = "2.03.98"
    categoria_pagar_alimentacao = "2.03.12"
    categoria_pagar_adiantamento = "2.03.02"
    categoria_pagar_previdencia = "2.03.14"
    return categoria_pagar_liquido,\
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
            categoria_pagar_previdencia

def categorias_invoice():
    """
        Retorna o código categoria de receitas para o Invoice
        param:  - None
        return: - categoria_receber_salario
                - categoria_receber_comissao
                - categoria_receber_dsr
                - categoria_receber_alimentacao
                - categoria_receber_reembolso_despesas
                - categoria_receber_reembolso_saude
                - categoria_receber_inss
                - categoria_receber_adiantamento
                - categoria_receber_previdencia
                - categoria_receber_inss_empresa
                - categoria_receber_fgts
                - categoria_receber_ferias
                - categoria_receber_decimo
                - categoria_receber_flash
                - categoria_invoice
                - categoria_receber_seguro
    """

    categoria_receber_salario = "1.01.98"
    categoria_receber_comissao = "1.01.87"
    categoria_receber_dsr = "1.01.95"
    categoria_receber_alimentacao = "1.01.03"
    categoria_receber_reembolso_despesas = "1.04.02"
    categoria_receber_reembolso_saude = "1.01.92"
    categoria_receber_inss = "1.01.91"
    categoria_receber_adiantamento = "1.04.01"
    categoria_receber_previdencia = "1.01.90"
    categoria_receber_inss_empresa = "1.01.89"
    categoria_receber_fgts = "1.01.88"
    categoria_receber_ferias = "1.01.97"
    categoria_receber_decimo = "1.01.94"
    categoria_receber_flash = "1.01.03"
    #categoria_invoice = "1.01.86"

    #=========== TESTE ===========#
    categoria_invoice = "1.01.89"
    #=========== TESTE ===========#

    categoria_receber_seguro = "1.01.85"

    return categoria_receber_salario,\
            categoria_receber_comissao,\
            categoria_receber_dsr,\
            categoria_receber_alimentacao,\
            categoria_receber_reembolso_despesas,\
            categoria_receber_reembolso_saude,\
            categoria_receber_inss,\
            categoria_receber_adiantamento,\
            categoria_receber_previdencia,\
            categoria_receber_inss_empresa,\
            categoria_receber_fgts,\
            categoria_receber_ferias,\
            categoria_receber_decimo,\
            categoria_receber_flash,\
            categoria_invoice,\
            categoria_receber_seguro
