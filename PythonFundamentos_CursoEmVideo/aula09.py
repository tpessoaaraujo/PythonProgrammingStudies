"""
** Manipulando Textos **

frase = 'Curso em Vídeo Python'

frase[9] # Acessa o caractere na posição 9
frase[9:13] # Acessa os caracteres da posição 9 até a posição 12 (13-1)
frase[9:21] # Acessa os caracteres da posição 9 até a posição 20 (21-1)

frase[9:21:2] # Acessa os caracteres da posição 9 até a posição 20 (21-1) pulando de 2 em 2
frase[:5] # Acessa os caracteres do início até a posição 4 (5-1)
frase[15:] # Acessa os caracteres da posição 15 até o final da string
frase[9::3] # Acessa os caracteres da posição 9 até o final da string pulando de 3 em 3

** Análise de Texto **

len(frase) # Retorna o número de caracteres da string
frase.count('o') # Conta quantas vezes a letra 'o' aparece na string
frase.count('o', 0, 13) # Conta quantas vezes a letra 'o' aparece na string entre as posições 0 e 12 (13-1)
frase.find('deo') # Retorna a posição onde a string 'deo' começa, ou -1 se não for encontrada
frase.find('Android') # Retorna -1, pois a string 'Android' não está presente na frase
'Curso' in frase # Retorna True, pois a string 'Curso' está presente na frase

** Transformação de Texto **

frase.replace('Python', 'Android') # Substitui a string 'Python' por 'Android'
frase.upper() # Converte a string para letras maiúsculas
frase.lower() # Converte a string para letras minúsculas
frase.capitalize() # Converte a primeira letra da string para maiúscula e as demais para minúsculas
frase.title() # Converte a primeira letra de cada palavra para maiúscula e as demais para minúsculas
frase.strip() # Remove os espaços em branco do início e do final da string
frase.rstrip() # Remove os espaços em branco do final da string
frase.lstrip() # Remove os espaços em branco do início da string

** Divisão de Texto **

frase.split() # Divide a string em uma lista de palavras
frase.split('o') # Divide a string em uma lista de substrings usando 'o' como separador

** Junção de Texto **

'-'.join(frase) # Junta os caracteres da string usando '-' como separador
"""

frase = 'Curso em Vídeo Python'

print(frase[9]) # Acessa o caractere na posição 9
print(frase[9:13]) # Acessa os caracteres da posição 9 até a posição 12 (13-1)
print(frase[9:21]) # Acessa os caracteres da posição 9 até a posição 20 (21-1)
print(frase[9:21:2]) # Acessa os caracteres da posição 9 até a posição 20 (21-1) pulando de 2 em 2
print(frase[:5]) # Acessa os caracteres do início até a posição 4 (5-1)
print(frase[15:]) # Acessa os caracteres da posição 15 até o final da string
print(frase[9::3]) # Acessa os caracteres da posição 9 até o final da string pulando de 3 em 3 
print(len(frase)) # Retorna o número de caracteres da string
print(frase.count('o')) # Conta quantas vezes a letra 'o' aparece na string
print(frase.count('o', 0, 13)) # Conta quantas vezes a letra 'o' aparece na string entre as posições 0 e 12 (13-1)
print(frase.find('deo')) # Retorna a posição onde a string 'deo' começa, ou -1 se não for encontrada
print(frase.find('Android')) # Retorna -1, pois a string 'Android' não está presente na frase
print('Curso' in frase) # Retorna True, pois a string 'Curso' está presente na frase
print(frase.replace('Python', 'Android')) # Substitui a string 'Python' por 'Android'
print(frase.upper()) # Converte a string para letras maiúsculas
print(frase.lower()) # Converte a string para letras minúsculas
print(frase.capitalize()) # Converte a primeira letra da string para maiúscula e as demais para minúsculas
print(frase.title()) # Converte a primeira letra de cada palavra para maiúscula e as demais para minúsculas
print(frase.strip()) # Remove os espaços em branco do início e do final da string
print(frase.rstrip()) # Remove os espaços em branco do final da string
print(frase.lstrip()) # Remove os espaços em branco do início da string
print(frase.split()) # Divide a string em uma lista de palavras
print(frase.split('o')) # Divide a string em uma lista de substrings usando 'o' como separador
print('-'.join(frase)) # Junta os caracteres da string usando '-' como separador
