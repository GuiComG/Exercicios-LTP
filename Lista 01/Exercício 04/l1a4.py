'''
Nome: Guilherme Nogueira Oliveira
Data: 07/08/2026
Enunciado: "Faça um Programa que peça as 4 notas bimestrais e mostre a média."
'''
# Entrada de Dados
notas = []

for i in range(4):
    notas.append(float(input("Me dê sua nota bimestral n° %i! > " %(i + 1))))

# Processamento de Dados

media = 0
index = 0

for item in notas:
    index = index + 1
    media = media + item

media = media / index

# Saída de Dados
print("Sua média foi %.2f!" %(float(media)))
