'''
Nome: Guilherme Nogueira Oliveira
Data: 07/08/2026
Enunciado: "Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês."
'''
# Entrada de Dados

dinheiroporhora = input("Me dê a quantidade que você ganha por hora! > ")
horastrabalhadas = input("Me dê suas horas trabalhadas por mês! > ")

# Processamento de Dados

salario = float(dinheiroporhora) * float(horastrabalhadas)

# Saída de Dados
print("Você ganha R$%.2f por mês!" %(float(salario)))
