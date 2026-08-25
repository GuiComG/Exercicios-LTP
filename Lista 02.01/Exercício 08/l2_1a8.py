'''
Nome: Guilherme Nogueira Oliveira
Data: 10/08/2026
Enunciado: "Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida."
'''
# Entrada de Dados

data = input("Me dê uma data (formato dd/mm/aaaa). > ")

# Processamento de Dados
validade = "Inválido!"
if len(data) == 10:
    dia = data[0] + data[1]
    mes = data[3] + data[4]
    ano = data[6] + data[7] + data[8] + data[9]
    try:
        float(mes)
        float(dia)
        float(ano)
        if (float(ano) % 4 == 0) or (float(ano) % 400 == 0):
            diasmeses = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            diasmeses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if float(mes) <= 12 and float(dia) <= diasmeses[int(mes) - 1]:
            validade = "Válido!"
    except ValueError:
        # Saída de Dados
        print("Não são números!")
# Saída de Dados        
print(validade)

