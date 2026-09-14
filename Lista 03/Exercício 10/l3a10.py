'''
Nome: Guilherme Nogueira Oliveira
Data: 14/09/2026
Enunciado: Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
'''
# Entrada / Processamento de dados
num1 = 50
num2 = 0
while num1 > num2:
    num1 = int(input("Me dê um número! > "))
    num2 = int(input("Me dê outro número maior que o número anterior! > "))
    if num1 > num2:
        print("Inválido!")
# Processamento / Saída de dados
index = num1 + 1
while index < num2:
    print(str(index))
    index += 1