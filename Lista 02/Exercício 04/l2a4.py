'''
Nome: Guilherme Nogueira Oliveira
Data: 10/08/2026
Enunciado: "Faça um Programa que verifique se uma letra digitada é vogal ou consoante."
'''
# Entrada de Dados

ltr = input("Insira uma letra: ")

# Processamento de Dados
vogais = ["a", "e", "i", "o", "u"]
consonantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
consonantevogal = ""
if ltr.lower() in vogais:
    consonantevogal = "uma vogal!"
elif ltr.lower() in consonantes:
    consonantevogal = "uma consonante!"
else:
    consonantevogal = "inválida!"
    
# Saída de Dados
print("Sua letra é %s" %(consonantevogal))
