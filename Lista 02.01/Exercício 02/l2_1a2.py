'''
Nome: Guilherme Nogueira Oliveira
Data: 10/08/2026
Enunciado: "Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato.
O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) Sindicato (3%)              : R$   33,00                          (Não tem desconto) FGTS (11%)           : R$  121,00
        Total de descontos              : R$   88,00
        Salário Liquido                 : R$  1012,00"
'''
# Entrada de Dados

horas = float(input("Me dê as suas horas trabalhadas. > "))
vph = float(input("Me dê o seu valor por hora. > "))
# Processamento de Dados

salariobruto = horas * vph

desconto = 0
descontotexto = "0%"
if salariobruto >= 900 and salariobruto < 1500:
    desconto= (salariobruto / 100) * 5
    descontotexto = "5%"
elif salariobruto >= 1500 and salariobruto < 2500:
    desconto = (salariobruto / 100)*10
    descontotexto = "10%"
elif salariobruto >= 2500:
    desconto = (salariobruto / 100)*20
    descontotexto = "20%"
Sindicato = (salariobruto / 100)*3
descontostotais = desconto + Sindicato
salarioliquido = salariobruto - descontostotais
# Saída de Dados
print('''
Salário Bruto:(%.1f * %.1f)     : R$ %.2f

(-) IR (%s)                     : R$   %.2f
(-) Sindicato (3%%)              : R$   %.2f
Total de descontos              : R$   %.2f
Salário Liquido                 : R$   %.2f
'''%(vph, horas, salariobruto, descontotexto, desconto, Sindicato, descontostotais, salarioliquido))
