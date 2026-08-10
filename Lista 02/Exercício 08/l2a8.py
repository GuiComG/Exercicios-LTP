'''
Nome: Guilherme Nogueira Oliveira
Data: 10/08/2026
Enunciado: "Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato."
'''
# Entrada de Dados

Num1 = input("Me dê o preço de um produto > ")
Num2 = input("Me dê o preço de outro produto. > ")
Num3 = input("Me dê o preço de um último produto. > ")

# Processamento de Dados

numeromenor = 0

if Num1 < Num2 and Num1 < Num3:
    numeromenor = "1"
if Num2 < Num3 and Num2 < Num1:
    numeromenor = "2"
if Num3 < Num1 and Num3 < Num2:
    numeromenor = "3"
    
# Saída de Dados

print("Você deverá comprar o produto n° %s!" %(numeromenor))
