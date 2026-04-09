""" 
** Condições **

if (se) # Condição simples
else (senao) # Condição composta
elif (senao se) # Condição encadeada
"""

n1 = float(input('Digite um número: '))
if n1 >= 0:
    print(f'O número {n1} é positivo.')
else:
    print(f'O número {n1} é negativo.')
    
n2 = float(input('Digite outro número: '))
if n2 >= 0:
    print(f'O número {n2} é positivo.')
elif n2 < 0:
    print(f'O número {n2} é negativo.')
else:
    print(f'O número {n2} é zero.')
