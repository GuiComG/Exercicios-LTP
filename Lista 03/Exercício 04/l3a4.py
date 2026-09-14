'''
Nome: Guilherme Nogueira Oliveira
Data: 14/09/2026
Enunciado:  Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% 
e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
'''
# Processamento de Dados
paisApop = 80000
paisBpop = 200000
index = 0
while paisApop < paisBpop:
    paisApop += (paisApop * 0.03)
    paisBpop += (paisBpop * 0.015)
    index += 1
# Saída de Dados
print(index)