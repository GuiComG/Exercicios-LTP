'''
Nome: Guilherme Nogueira Oliveira
Data: 07/08/2026
Enunciado: "Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário."
'''
# Entrada de Dados

lado = input("Me dê o lado de um quadrado! > ")

# Processamento de Dados

area = float(lado) ** 2
area = area * 2

# Saída de Dados
print("O dobro da área do quadrado é %.2f!" %(float(area)))
