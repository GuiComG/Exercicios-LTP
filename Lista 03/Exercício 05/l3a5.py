'''
Nome: Guilherme Nogueira Oliveira
Data: 14/09/2026
Enunciado: Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
'''
# Entrada / Processamento / Saída de Dados
while True:
    paisApop = 0
    paisBpop = -1
    while paisApop > paisBpop:
        paisApop = int(input("Me dê a população de um país! > "))
        paisBpop = int(input("Me dê outra população maior quea população anterior! > "))
        if paisApop > paisBpop:
            print("Inválido!")
    paisAcre = 0
    paisBcre = 1
    while paisAcre <= paisBcre:
        paisAcre = int(input("Me dê uma taxa de crescimento! (%) > "))
        paisBcre = int(input("Me dê outra taxa de crescimento menor que a taxa de crescimento anterior! (%) > "))
        if paisAcre <= paisBcre:
            print("Inválido!")
    index = 0
    while paisApop < paisBpop:
        paisApop += (paisApop * (paisAcre / 100))
        paisBpop += (paisBpop * (paisBcre / 100))
        index += 1
    print("Demorará %d anos para a população do primeiro país ser maior que a população do segundo país!" %(index))