'''
Nome: Guilherme Nogueira Oliveira
Data: 10/08/2026
Enunciado: "As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento."
'''
# Entrada de Dados

salario = float(input("Me dê o seu salário. > "))

# Processamento de Dados

if salario <= 280:
    nsalario = (salario / 100)*120
    aumento = "20%"
elif salario > 280 and salario <= 700:
    nsalario = (salario / 100)*115
    aumento = "15%"
elif salario > 700 and salario <= 1500:
    nsalario = (salario / 100)*110
    aumento = "10%"
elif salario > 1500:
    nsalario = (salario / 100)*105
    aumento = "5%"
aumentovalor = nsalario - salario
# Saída de Dados
print("O seu salário anterior era de %.2f, foi aplicado um aumento de %s, adicionando %.2f ao seu salário. Agora, você tem um salário de %.2f." %(salario, aumento, aumentovalor, nsalario))
