'''
** Condições Aninhadas **

if (se) # Condição simples
else (senao) # Condição composta
elif (senao se) # Condição encadeada
'''

nome = str(input('Digite seu nome: '))
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
elif nome == 'Maria' or nome == 'Ana' or nome == 'João':
    print('Seu nome é bem popular no Brasil.')
else:
    print('Seu nome é bem normal.')
print(f'Prazer em te conhecer, {nome}!')
