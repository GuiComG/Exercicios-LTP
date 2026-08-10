'''
Nome: Guilherme Nogueira Oliveira
Data: 10/08/2026
Enunciado: "Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16"
'''
# Entrada de Dados
inteiro = 1243
while inteiro > 999:
    inteiro = int(input("Me dê um número inteiro menor que 1000. > "))

# Processamento de Dados
centenas = ""
dezenas = ""
unidades = ""
if len(str(inteiro)) == 3:
    centenas = str(inteiro)[0]
    dezenas = str(inteiro)[1]
    unidades = str(inteiro)[2]
    # Saída de Dados      
    print("O seu número possui %s centenas, %s dezenas e %s unidades." %(centenas, dezenas, unidades))
if len(str(inteiro)) == 2:
    dezenas = str(inteiro)[0]
    unidades = str(inteiro)[1]
    # Saída de Dados      
    print("O seu número possui %s dezenas e %s unidades." %(dezenas, unidades))
if len(str(inteiro)) == 1:
    unidades = str(inteiro)[0]
    # Saída de Dados      
    print("O seu número possui %s unidades." %(unidades))
    
