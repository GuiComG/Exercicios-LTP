'''
Nome: Guilherme Nogueira Oliveira
Data: 10/08/2026
Enunciado: "Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido."
'''
# Entrada de Dados

sx = input("Insira o seu sexo.(F/M) > ")

# Processamento de Dados
sxtxt = "" 
if sx == "F":
    sxtxt = "Feminino"
elif sx == "M":
    sxtxt = "Masculino"
else:
    sxtxt = "Sexo Inválido"
    
# Saída de Dados
print("Você inseriu: %s" %(sxtxt))
