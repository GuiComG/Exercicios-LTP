'''
Nome: Guilherme Nogueira Oliveira
Data: 10/08/2026
Enunciado: "Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo."
'''
# Entrada de Dados

num = float(input("Me dê um número. > "))

# Processamento de Dados

posneg = ""
if num > 0:
    posneg = "positivo"
elif num < 0:
    posneg = "negativo"
elif num == 0:
    posneg = "neutro"
    
# Saída de Dados

print("O número dado é %s!" %(posneg))
