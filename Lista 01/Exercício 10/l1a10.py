'''
Nome: Guilherme Nogueira Oliveira
Data: 07/08/2026
Enunciado: "Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit."
'''
# Entrada de Dados

C = input("Me dê uma temperatura em Celsius! > ")

# Processamento de Dados

F = float(C) * 1.8 + 32

# Saída de Dados
print("A temperatura em Fahrenheit é %.2f °F!" %(float(F)))
