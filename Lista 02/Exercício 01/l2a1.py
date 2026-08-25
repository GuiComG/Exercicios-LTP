'''
Nome: Guilherme Nogueira Oliveira
Data: 10/08/2026
Enunciado: "Faça um Programa que peça dois números e imprima o maior deles."
'''
# Entrada de Dados

Num1 = float(input("Me dê um número. > "))
Num2 = float(input("Me dê outro número. > "))

# Processamento de Dados

numeromaior = 0
numeromenor = 0

if Num1 > Num2:
    numeromaior = Num1
    numeromenor = Num2
else:
    numeromaior = Num2
    numeromenor = Num1

# Saída de Dados

print("%.1f é maior que %.1f!" %(numeromaior, numeromenor))
