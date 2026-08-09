'''
Nome: Guilherme Nogueira Oliveira
Data: 09/08/2026
Enunciado: "Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. "
'''
# Entrada de Dados
metrospintados = float(input("Me dê o tamanho em metros quadrados da área a ser pintada! > "))
# Processamento de Dados
import math
litrostotais = float(metrospintados / 3)

latas18totais = math.ceil(litrostotais / 18)
latas18totaispreco = latas18totais * 80

latas3_6totais = math.ceil(litrostotais / 3.6)
latas3_6totaispreco = latas3_6totais * 25


litrostotaisfolga = ((litrostotais / 100) * 110)
latasmisturadas = int((litrostotaisfolga // 18) + (math.ceil((litrostotaisfolga % 18) / 3.6)))
latasmisturadaspreco = ((litrostotaisfolga // 18) * 80) + (math.ceil((litrostotaisfolga % 18) / 3.6) * 25)
# Saída de Dados
print("Você terá que comprar %.2f litros de tinta! Ou seja," %(litrostotais))
print(latas18totais, "latas de 18 litros custando R$",latas18totaispreco)
print(latas3_6totais, "latas de 3.6 litros custando R$",latas3_6totaispreco)
print(latasmisturadas, "latas misturadas custando R$",latasmisturadaspreco)

