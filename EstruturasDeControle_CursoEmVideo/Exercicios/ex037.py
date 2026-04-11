# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: binário, octal ou hexadecimal.

num = int(input("Digite um número: "))

print("1 - Binário")
print("2 - Octal")
print("3 - Hexadecimal")
base = int(input("Qual a base que seja para conversão? "))

if base == 1:
    print(bin(num)[2:])
elif base == 2:
    print(oct(num)[2:])
elif base == 3:
    print(hex(num)[2:])
else:
    print("Opção selecionada incorreta. Tente novamente.")
