# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior; O segundo valor é maior; Não existe valor maior, os dois são iguais.

num1 = int(input("Digite um número: "))
num2 = int(input("Digita outro número: "))

if num1 > num2:
    print("O número {} (primeiro valor) é maior que {} (segundo valor).".format(num1, num2))
elif num1 < num2:
    print("O número {} (primeiro valor) é menor que {} (segundo valor).".format(num1, num2))
else:
    print("Os dois números digitados são iguais.")
