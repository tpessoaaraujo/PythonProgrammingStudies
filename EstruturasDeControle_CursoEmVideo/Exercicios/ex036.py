# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do saláro ou então o empréstimo será negado.

valorCasa = float(input('Valor da casa: R$ '))
salarioComprador = float(input('Salário do comprador: R$ '))
anosFinanciamento = int(input('Quantos anos de financiamento? '))

mesesFinanciamento = anosFinanciamento * 12
valorParcela = valorCasa / mesesFinanciamento

if valorParcela > (salarioComprador * 0.3):
    print("O valor da parcela é de R$ {:.2f} e está acima da margem permitida. Empréstimo negado.".format(valorParcela))
else:
    print("O valor da parcela é de R$ {:.2f} e está dentro da margem permitida. Empréstimo aprovado.".format(valorParcela))
