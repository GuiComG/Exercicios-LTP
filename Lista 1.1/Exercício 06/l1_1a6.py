'''
Nome: Guilherme Nogueira Oliveira
Data: 09/08/2026
Enunciado: "Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.  "
'''
# Entrada de Dados
metrospintados = float(input("Me dê o tamanho em metros quadrados da área a ser pintada! > "))
# Processamento de Dados
import math
litrostotais = metrospintados / 3
latas = int(math.ceil(litrostotais / 18))
precototal = latas * 80
# Saída de Dados
print("Você irá comprar",latas,"lata(s), lhe custando R$",precototal,"no total.")

