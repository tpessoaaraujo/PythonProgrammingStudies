"""
** Cores no Terminal **

\033[style;text;backm] # estilo, texto, fundo

Estilos:
0: Normal
1: Negrito
4: Sublinhado
7: Inverter

Textos:
30: Branco
31: Vermelho
32: Verde
33: Amarelo
34: Azul
35: Magenta
36: Ciano
37: Cinza

Fundos:
40: Branco
41: Vermelho
42: Verde
43: Amarelo
44: Azul
45: Magenta
46: Ciano
47: Cinza

\033[0;33;44m] # estilo 0, texto amarelo, fundo azul
\033[4;30;45m] # estilo 4, texto preto, fundo magenta
\033[1;35;43m] # estilo 1, texto magenta, fundo amarelo
"""

print('\033[0;33;44mOlá, Mundo!\033[m') # estilo 0, texto amarelo, fundo azul
print('\033[4;30;45mOlá, Mundo!\033[m') # estilo 4, texto preto, fundo magenta
print('\033[1;35;43mOlá, Mundo!\033[m') # estilo 1, texto magenta, fundo amarelo
print('\033[1;31;43mOlá, Mundo!\033[m') # estilo 1, texto vermelho, fundo amarelo
print('\033[1;30;42mOlá, Mundo!\033[m') # estilo 1, texto preto, fundo verde
