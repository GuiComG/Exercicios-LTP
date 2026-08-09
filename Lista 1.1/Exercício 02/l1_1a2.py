'''
Nome: Guilherme Nogueira Oliveira
Data: 07/08/2026
Enunciado: "Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58"
'''
# Entrada de Dados

altura = float(input("Me dê a sua altura! > "))


# Processamento de Dados

pesoideal = (72.7*altura) - 58

# Saída de Dados
print("Seu peso ideal seria %.2f!" %(float(pesoideal)))
