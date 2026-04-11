# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# Entre 25 até 30: Sobrepeso
# Entre 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida

peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (m): "))

imc = peso / (altura ** 2)

print("IMC: {:.1f}".format(imc))
if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc > 18.5 and imc <= 25:
    print("Você está no pesoa ideal.")
elif imc > 25 and imc <= 30:
    print("Você está com sobrepeso.")
else:
    print("Você está com obesidade mórbida.")
