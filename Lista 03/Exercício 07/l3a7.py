'''
Nome: Guilherme Nogueira Oliveira
Data: 14/09/2026
Enunciado: Faça um programa que leia 5 números e informe o maior número.
'''
# Entrada / Processamento de Dados
index = 0
while index != 5:
    biggernumber = "a"
    index += 1
    num = int(input("Me dê um número! > "))
    if biggernumber == "a" or num > biggernumber:
        biggernumber = num
# Saída de Dados
print("O maior número é %d." %(biggernumber))
    