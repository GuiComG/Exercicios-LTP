'''
Nome: Guilherme Nogueira Oliveira
Data: 09/08/2026
Enunciado: "Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
faça um programa que nos dê:
A. salário bruto.
B. quanto pagou ao INSS.
C. quanto pagou ao sindicato.
D. o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
"
'''
# Entrada de Dados
dinheiroporhora = float(input("Me dê quanto você ganha por hora! > "))
horastrabalhadas = int(input("Me dê quantas horas você trabalhou por! > "))
# Processamento de Dados
salariobruto = dinheiroporhora * horastrabalhadas
INSS = (salariobruto / 100) * 8
IR = (salariobruto / 100) * 11
sindicato = (salariobruto / 100) * 5
salarioliquido = salariobruto - (IR + INSS + sindicato)

# Saída de Dados
print("Seu salário bruto é R$%.2f." %(salariobruto))
print("Você irá pagar R$%.2f ao INSS." %(INSS))
print("Você irá pagar R$%.2f ao sindicato." %(sindicato))
print("seu salário líquido será de R$%.2f." %(salarioliquido))
