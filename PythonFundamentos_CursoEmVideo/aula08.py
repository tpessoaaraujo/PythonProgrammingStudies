""" 
** Utilizando Módulos **

Importando um módulo inteiro
import math
print(math.sqrt(16))

Importando apenas uma função de um módulo
from math import sin
print(sin(90))
"""

import math
n1 = int(input('Digite um número: '))
raiz = math.sqrt(n1)
print(f'A raiz quadrada de {n1} é {raiz:.2f}')

from math import sin
n2 = int(input('Digite um número: '))
seno = sin(n2)
print(f'O seno de {n2} é {seno:.2f}')
