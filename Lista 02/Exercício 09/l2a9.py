'''
Nome: Guilherme Nogueira Oliveira
Data: 10/08/2026
Enunciado: "Faça um Programa que leia três números e mostre-os em ordem decrescente."
'''
# Entrada de Dados


Num1 = float(input("Me dê um número. > "))
Num2 = float(input("Me dê outro número. > "))
Num3 = float(input("Me dê um último número. > "))

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

numeromeio = 0

listanumeros = [Num1, Num2, Num3]
listanumeros.remove(numeromaior)
listanumeros.remove(numeromenor)
    
# Saída de Dados

print("Os números, em ordem decrescente são: %.1f, %.1f e %.1f." %(numeromaior, listanumeros[0], numeromenor))
