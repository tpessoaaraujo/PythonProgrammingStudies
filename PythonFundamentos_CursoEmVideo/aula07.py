"""
Operados Aritméticos:
+ Adição
- Subtração
* Multiplicação
/ Divisão
// Divisão Inteira
% Resto da Divisão
** Potência
"""
print(10 + 10)  # Adição
print(10 - 10)  # Subtração
print(10 * 10)  # Multiplicação
print(10 / 10)  # Divisão
print(10 // 3)  # Divisão Inteira
print(10 % 3)  # Resto da Divisão
print(10 ** 2)  # Potência

"""
Ordem de Precedência:
1. Parênteses
2. Potência
3. Multiplicação e Divisão
4. Adição e Subtração
"""

print((10 + 10) * 10)  # Parênteses tem precedência
print(10 + 10 * 10 ** 2)  # Potência tem precedência
print(10 + 10 * 10)  # Multiplicação tem precedência
print(10 + 10 - 10)  # Adição e Subtração tem a mesma precedência, então é feita da esquerda para a direita
