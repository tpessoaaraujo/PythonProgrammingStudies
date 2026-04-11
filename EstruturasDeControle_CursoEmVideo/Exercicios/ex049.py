# Faça um programa mostrando a tabuada de um número que o usuário escolhe utilizando o laço for.

num = int(input('Digite um número: '))

for c in range (1, 11, 1):
    resultado = num * c
    print("{} x {} = {}".format(num, c, resultado))
print('Fim')
