# Tipos Primitivos e Saída de Dados

"""
int = 7, -4, 0, 9875
float = 4.5, 0.076, -15.223, 7.0
bool = True, False
str = 'Olá', 'True', '7.5', ''
"""

n1 = int(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
soma = n1 + n2

print('A soma entre {} e {} é igual a {}'.format(n1, n2, soma))

print(type(n1)) # Número inteiro (int)
print(type(n2)) # Número real (float)
print(type(soma)) # A soma entre um inteiro (int) e um real (float) é sempre um real (float)

"""
n.isalnum() -> Verifica se é alfanumérico
n.isdecimal() -> Verifica se é decimal
n.isdigit() -> Verifica se é um dígito
n.isnumeric() -> Verifica se é numérico

n.isprintable() -> Verifica se é imprimível
n.isalpha() -> Verifica se é alfabético
n.istitle() -> Verifica se é um título
n.isupper() -> Verifica se é maiúsculo
n.islower() -> Verifica se é minúsculo
n.isspace() -> Verifica se é um espaço em branco
n.isidentifier() -> Verifica se é um identificador
n.isascii() -> Verifica se é um caractere ASCII
"""
