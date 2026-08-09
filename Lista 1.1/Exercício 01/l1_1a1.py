'''
Nome: Guilherme Nogueira Oliveira
Data: 07/08/2026
Enunciado: "Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo."
'''
# Entrada de Dados

Inteiro = int(input("Me dê um número inteiro! > "))
Real1 = float(input("Me dê um número real! > "))
Real2 = float(input("Me dê um outro número real! > "))

# Processamento de Dados

a = (2 * Inteiro) * (Real1 / 2)
b = (Inteiro * 3) + (Real2)
c = (Real2 ** 3)

# Saída de Dados
print("O produto do dobro do número inteiro com metade do primeiro número real é %.2f." %(float(a)))
print("A soma do triplo do número inteiro om o segundo número real é %.2f." %(float(b)))
print("O segundo número real elevado ao cubo é %.2f." %(c))
