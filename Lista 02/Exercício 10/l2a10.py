'''
Nome: Guilherme Nogueira Oliveira
Data: 10/08/2026
Enunciado: "Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso."
'''
# Entrada de Dados

trn = input("Insira o turno em que você estuda.(M/V/N) > ")

# Processamento de Dados
trntxt = "" 
if trn == "M":
    trntxt = "Bom Dia!"
elif trn == "V":
    trntxt = "Boa Tarde!"
elif trn == "N":
    trntxt = "Boa noite!"
else:
    trntxt = "Valor Inválido!"
    
# Saída de Dados
print("%s" %(trntxt))
