from datetime import datetime

registros = []

def criar_registro(tipo, valor, data):
    data_registro = datetime.strptime(data, "%d/%m/%Y").date()
    dia, mes, ano = data_registro.day, data_registro.month, data_registro.year

    if tipo == 'Receita':
        valor = float(valor)
        montante = 0
    elif tipo == 'Despesas':
        valor = -float(valor)
        montante = 0
    elif tipo == 'Investimento':
        valor = float(valor)
        montante = valor * (1 + 0.02) ** ((datetime.now().date() - data_registro).days) - valor
    else:
        raise ValueError("Tipo de movimentação inválido.")

    registro = {'tipo': tipo, 'valor': valor, 'dia': dia, 'mes': mes, 'ano': ano, 'montante': montante}
    registros.append(registro)

def ler_registros():

def atualizar_registro():

def deletar_registro():

def atualiza_rendimento():
