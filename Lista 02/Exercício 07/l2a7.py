'''
Nome: Guilherme Nogueira Oliveira
Data: 10/08/2026
Enunciado: "Faça um Programa que leia três números e mostre o maior e o menor deles."
'''
# Entrada de Dados

Num1 = input("Me dê um número. > ")
Num2 = input("Me dê outro número. > ")
Num3 = input("Me dê um último número. > ")

# Processamento de Dados

numeromaior = 0

if Num1 > Num2 and Num1 > Num3:
    numeromaior = Num1
if Num2 > Num3 and Num2 > Num1:
    numeromaior = Num2
if Num3 > Num1 and Num3 > Num2:
    numeromaior = Num3

numeromenor = 0

if Num1 < Num2 and Num1 < Num3:
    numeromenor = Num1
if Num2 < Num3 and Num2 < Num1:
    numeromenor = Num2
if Num3 < Num1 and Num3 < Num2:
    numeromenor = Num3
    
# Saída de Dados

print("O número maior entre os 3 é %.1f!" %(float(numeromaior)))
print("O número menor entre os 3 é %.1f!" %(float(numeromenor)))
