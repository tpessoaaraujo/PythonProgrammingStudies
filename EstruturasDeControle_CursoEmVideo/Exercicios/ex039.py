# Faça um programa que leia o ano de nascimento de um jovem e informa, de acordo com a sua idade:
# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar
# - Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date

anoNascimento = int(input("Digite o seu ano de nascimento: "))
anoAtual = date.today().year

idade = anoAtual - anoNascimento

if idade < 18:
    tempoRestante = 18 - idade
    print("Você ainda irá se alistar no serviço militar em {} anos.".format(tempoRestante))
elif idade > 18:
    tempoAtraso = idade - 18
    print("Você já passou do tempo de alistamento em {} anos.".format(tempoAtraso))
else:
    print("Esta na hora de você se alistar!")
