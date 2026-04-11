'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

opcao = 4
while opcao == 4:
    num1 = float(input('Digite o primeiro valor: '))
    num2 = float(input('Digite o segundo valor: '))
    print('''
          [1] somar
          [2] multiplicar
          [3] maior
          [4] novos números
          [5] sair do programa
          ''')
    opcao = int(input('O que você deseja fazer? '))
    if opcao == 1:
        soma = num1 + num2
        print("A soma de {} + {} é igual a {}".format(num1, num2, soma))
    elif opcao == 2:
        multi = num1 * num2
        print("A multiplicação de {} x {} é igual a {}".format(num1, num2, multi))
    elif opcao == 3:
        if num1 > num2:
            print("O número {} é o maior.".format(num1))
        elif num1 < num2:
            print("O número {} é o maior.".format(num2))
        else:
            print("Os números são iguais.")
    elif opcao == 4:
        print("Digite os novos números abaixo.")
    elif opcao == 5:
            print("Encerrando o programa.")
            break
    else:
        print("Opção incorreta. Tente novamente.")
        opcao = 4
