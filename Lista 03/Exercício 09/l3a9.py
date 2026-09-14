'''
Nome: Guilherme Nogueira Oliveira
Data: 14/09/2026
Enunciado: Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
'''
# Entrada / Processamento / Saída de Dados
index = 0
while index < 50:
    index += 1
    if (index % 2 != 0):
        print(index)