'''
Nome: Guilherme Nogueira Oliveira
Data: 10/08/2026
Enunciado: "Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido."
'''
# Entrada de Dados

dia = int(input("Me dê um número. > "))
# Processamento de Dados
listadias = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
diasemana = "Valor Inválido"
if dia < 8 and dia > 0:
    diasemana = listadias[dia - 1]

# Saída de Dados
print("O dia da semana com esse número é %s." %(diasemana))
