'''
Nome: Guilherme Nogueira Oliveira
Data: 14/09/2026
Enunciado: Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
'''
# Entrada / Processamento de Dados
z = 11 
while z < 0 or z > 10:
    z = float(input("Me dê uma nota entre zero e dez! > "))
    if z < 0 or z > 10:
        print("Valor Inválido!")
# Saída de Dados
print("Ok, Obrigado!")