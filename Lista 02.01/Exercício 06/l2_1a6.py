'''
Nome: Guilherme Nogueira Oliveira
Data: 10/08/2026
Enunciado: "Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;"
'''
# Entrada de Dados
import math

A = float(input("Me dê o valor de a. > "))
B = float(input("Me dê o valor de b. > "))
C = float(input("Me dê o valor de c. > "))

# Processamento de Dados

consistencia = ""
delta = ""
if A == 0:
    consistencia = "A equação nao possui raízes reais."
else:
    delta = (B ** 2) - (4 * A * C)
    if delta < 0:
        consistencia = "A equação não possui raízes reais."
    if delta == 0:
        raiz = (-B + math.sqrt(delta)) / (2 * A)
        consistencia = ("A equação possui uma raiz, sendo %.2f." %(raiz))
    if delta > 0:
        raiz1 = (-B + math.sqrt(delta)) / (2 * A)
        raiz2 = (-B - math.sqrt(delta)) / (2 * A)
        consistencia = ("A equação possui duaz raízes, sendo %.2f e %.2f." %(raiz1, raiz2))
    
# Saída de Dados

print(consistencia)
