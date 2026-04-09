# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan
angulo = float(input('Digite um ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O seno de {angulo} é {seno:.2f}')
print(f'O cosseno de {angulo} é {cosseno:.2f}')
print(f'A tangente de {angulo} é {tangente:.2f}')
