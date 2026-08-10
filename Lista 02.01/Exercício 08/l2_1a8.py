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
        if float(mes) <= 12 and float(dia) <= 30:
            validade = "Válido!"
    except ValueError:
        # Saída de Dados
        print("Não são números!")
# Saída de Dados        
print(validade)

