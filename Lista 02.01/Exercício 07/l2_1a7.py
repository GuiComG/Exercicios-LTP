'''
Nome: Guilherme Nogueira Oliveira
Data: 10/08/2026
Enunciado: "Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto."
'''
# Entrada de Dados

ano = float(input("Me dê um ano. > "))

# Processamento de Dados
bissexto = "O seu ano não é bissexto."
if (ano % 4 == 0 and ano % 100 != 0 ) or (ano % 400 == 0):
    bissexto = "O seu ano é bissexto."
# Saída de Dados
print(bissexto)

