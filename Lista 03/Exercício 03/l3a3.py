'''
Nome: Guilherme Nogueira Oliveira
Data: 14/09/2026
Enunciado: Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''
# Entrada / Processamento / Saída de Dados
nome = ""
while nome == "":
    nome = str(input("Me dê o seu nome! > "))
    if nome == "" or len(nome) <= 2:
        print("Nome Inválido!")
        nome = ""
Idade = -1
while Idade < 0 or Idade > 122:
    Idade = int(input("Me dê sua idade! > "))
    if Idade < 0 or Idade > 122:
        print("Idade Inválida!")
        Idade = -1
Salario = -1
while Salario <= 0:
    Salario = float(input("Me dê seu salário! > "))
    if Salario <= 0:
        print("Salário Inválido!")
        Salario = -1
sexo = ""
while sexo != "f" and sexo != "m":
    sexo = str(input("Me dê o seu sexo! (f / m) > "))
    if sexo != "f" and sexo != "m":
        print("Sexo Inválido! (O nosso sistema só suporta os sexos feminino (f) e masculino (m). Desculpe pelo transtorno!)")
        sexo = ""
EstadoCivil = ""
while EstadoCivil != "s" and EstadoCivil != "c" and EstadoCivil != "v" and EstadoCivil != "d" :
    EstadoCivil = str(input("Me dê o seu Estado civil! (s / c / v / d) > "))
    if EstadoCivil != "s" and EstadoCivil != "c" and EstadoCivil != "v" and EstadoCivil != "d":
        print("Estado civil Inválido!")
        EstadoCivil = ""
print("Ok, Obrigado!")