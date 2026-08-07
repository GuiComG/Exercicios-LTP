'''
Nome: Guilherme Nogueira Oliveira
Data: 07/08/2026
Enunciado: "Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius."
'''
# Entrada de Dados

F = input("Me dê uma temperatura em Fahrenheit! > ")

# Processamento de Dados

C = (5 * (float(F)-32) / 9)

# Saída de Dados
print("A temperatura em Celsius é %.2f °C!" %(float(C)))
