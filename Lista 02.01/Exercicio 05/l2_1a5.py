'''
Nome: Guilherme Nogueira Oliveira
Data: 10/08/2026
Enunciado: "Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;"
'''
# Entrada de Dados


Num1 = float(input("Me dê um lado. > "))
Num2 = float(input("Me dê outro lado. > "))
Num3 = float(input("Me dê um último lado. > "))

# Processamento de Dados

triangulo = "não é válido."

if Num1 + Num2 > Num3 and Num2 + Num3 > Num1 and Num1 + Num3 > Num2:
    triangulo = "é válido."
    if Num1 == Num2 and Num2 == Num3 and Num1 == Num3:
        triangulo = "é válido, sendo um triângulo equilátero."
    elif Num1 == Num2 or Num2 == Num3 or Num1 == Num3:
        triangulo = "é válido, sendo um triângulo isósceles."
    if Num1 != Num2 and Num2 != Num3 and Num1 != Num3:
        triangulo = "é válido, sendo um triângulo escaleno."
    
# Saída de Dados

print("O seu triângulo %s" %(triangulo))
