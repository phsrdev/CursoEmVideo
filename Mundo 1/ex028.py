'''print('-'*15, 'Desafio 028', '-'*15)
print('Vou pensar em um numero entre 0 e 5, tente advinhar...')
n = int(input('Em que numero eu pensei? '))
if n==0:
    print('Voce me venceu, parabens!')
else:
    print('Voce perdeu, eu pensei no 0')'''
from random import randint
print('-=-'*10, 'Desafio 028', '-=-'*10)
cpu = randint(0, 5)
print('Vou pensar em um numero entre 0 e 5, tente advinhar: ')
print('-=-'*25)
n = int(input('Em que numero eu pensei?'))
from time import sleep
print('Processando...')
sleep(3)
if n == cpu:
    print('Parabens! Voce acertou')
else:
    print('Você errou, eu pensei no {}'.format(cpu))


