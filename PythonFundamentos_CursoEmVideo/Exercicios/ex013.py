# Faça um algoritmo que leiia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Salário do funcionário: R$'))
aumento = salario * 0.15
novo_salario = salario + aumento

print(f'O funcionário que ganhava R${salario:.2f}, com o aumento de 15% vai passar a ganhar R${novo_salario:.2f}.')
