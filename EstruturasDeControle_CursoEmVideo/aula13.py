"""
    ** Estrutura de Repetição for **
    
    for c in range (0,6):
        print("6 repetições iguais")
    print("Fim")
    
    for c in range (6, 0, -1) # 5, 4, 3, 2, 1, 0
        print(c)
    print("Fim")
"""

i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))

for c in range(i, f+1, p):
    print(c)
print("Fim")

s = 0
for c in range(0, 4):
    n = int(input('Digite um número: '))
    s += n
print('O somatório de todos os valores foi {}.'.format(s))
