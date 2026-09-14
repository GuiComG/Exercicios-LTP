'''
Nome: Guilherme Nogueira Oliveira
Data: 14/09/2026
Enunciado: Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''
# Entrada / Processamento / Saída de Dados
nome = ""
while nome == "":
    nome = str(input("Me dê o seu nome! > "))
    if nome == "":
        print("Nome Inválido!")
Senha = ""
while Senha == "":
    Senha = str(input("Me dê uma senha! > "))
    if Senha == "" or Senha == nome:
        print("Senha Inválida!")
        Senha = ""
print("Ok, Obrigado!")