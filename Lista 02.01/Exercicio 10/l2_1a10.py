'''
Nome: Guilherme Nogueira Oliveira
Data: 10/08/2026
Enunciado: "Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10."
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
media = (nota1 + nota2) / 2
if media >= 7:
    aprovacao = ("Aprovado (média = %.1f)" %(media))
elif media < 7:
    aprovacao = ("Reprovado (média = %.1f)" %(media))
if media == 10:
    aprovacao = "Aprovado com Distinção"

# Saída de Dados
print("Você foi %s." %(aprovacao))
