import random
print('-'*15, 'Desafio 020', '-'*15)
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
list = [n1, n2, n3, n4]
random.shuffle(list)
print('A ordem de apresentação será:')
print(list)