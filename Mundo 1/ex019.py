import random
print('-'*15, 'Desafio 019', '-'*15)
n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))
list = [n1, n2, n3, n4]
choice = random.choice(list)
print('O aluno escolhido foi {}.'.format(choice))
