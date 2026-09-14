'''
Nome: Guilherme Nogueira Oliveira
Data: 14/09/2026
Enunciado: Faça um programa que leia 5 números e informe a soma e a média dos números.
'''
# Entrada / Processamento de Dados
index = 0
lst = []
while index != 5:
    index += 1
    num = float(input("Me dê um número! > "))
    lst.append(num)
index = 0
sum = 0
while index < len(lst):
    sum += lst[index]
    index += 1
medium = sum / index
# Saída de Dados
print("A soma dos números é de %.1f." %(sum))
print("A média dos números é de %.1f." %(medium))
    