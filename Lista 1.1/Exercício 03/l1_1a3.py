'''
Nome: Guilherme Nogueira Oliveira
Data: 07/08/2026
Enunciado: "Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7 (h = altura)
Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso. 
"
'''
# Entrada de Dados

altura = float(input("Me dê a sua altura! > "))
peso = float(input("Me dê o seu peso! > "))
sexo = ""
while sexo != "M"  and sexo != "F":
    sexo = str(input("Me dê o seu sexo! (HOMEM: M / MULHER: F) > "))


# Processamento de Dados
pesoideal = 0

if sexo == "M":
    pesoideal = (72.7 * altura) - 58
if sexo == "F":
    pesoideal = (62.1 * altura) - 44.7


# Saída de Dados
print("O seu peso ideal é %.2f." %(pesoideal))
if peso > pesoideal:
    print("Você está acima do peso!")
if peso < pesoideal:
    print("Você está abaixo do peso!")
if peso == pesoideal:
    print("Você está dentro do peso!")
