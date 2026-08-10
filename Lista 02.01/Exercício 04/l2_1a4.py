'''
Nome: Guilherme Nogueira Oliveira
Data: 10/08/2026
Enunciado: "Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E."
'''
# Entrada de Dados
nota1 = 50
nota2 = 50
while nota1 > 10 or nota2 > 10:
    nota1 = float(input("Insira uma nota: "))
    nota2 = float(input("Insira outra nota: "))
    # Processamento de dados
    if nota1 > 10 or nota2 > 10:
        # Saída de dados
        print("Notas inválidas! Insira um número menor ou igual a 10!")

# Processamento de Dados
aprovacao = ""
conceito = ""
media = (nota1 + nota2) / 2
if media >=9 and media <= 10:
    aprovacao = "APROVADO"
    conceito = "A"
elif media < 9 and media >= 7.5:
    aprovacao = "APROVADO"
    conceito = "B"
elif media < 7.5 and media >= 6:
    aprovacao = "APROVADO"
    conceito = "C"
elif media < 6 and media >= 4:
    aprovacao = "REPROVADO"
    conceito = "D"
elif media < 4:
    aprovacao = "REPROVADO"
    conceito = "E"


# Saída de Dados
print("Você tirou as notas %.1f e %.1f, tendo uma média de %.1f. Você recebeu o conceito %s. Você foi %s." %(nota1, nota2, media, conceito, aprovacao))
