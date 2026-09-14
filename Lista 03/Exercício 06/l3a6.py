'''
Nome: Guilherme Nogueira Oliveira
Data: 14/09/2026
Enunciado: Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.
'''
# Entrada / Processamento / Saída de Dados
index = 0
while index != 20:
    index += 1
    print(index)
index = 0
numstr = ""
while index != 20:
    index += 1
    numstr += str(index)
print(numstr)