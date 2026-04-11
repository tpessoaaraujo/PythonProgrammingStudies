# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

opcoes = ("Pedra", "Papel", "Tesoura")
escolhaComputador = randint(0, 2)

print(""" Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA""")

escolhaJogador = int(input("Qual é a sua jogada? "))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")

print("-=" * 11)
print("Computador jogou {}.".format(opcoes[escolhaComputador]))
print("Jogador jogou {}.".format(opcoes[escolhaJogador]))
print("-=" * 11)

if escolhaComputador == escolhaJogador:
    print("EMPATE!")
elif escolhaComputador == 1 and escolhaJogador == 2 or escolhaComputador == 2 and escolhaJogador == 3 or escolhaComputador == 3 and escolhaJogador == 1:
    print("VITÓRIA DO JOGADOR!")
else:
    print("VITÓRIA DO COMPUTADOR!")
