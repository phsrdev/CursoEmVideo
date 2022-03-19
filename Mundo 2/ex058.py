print('-='*15, 'Desafio 058', '-='*15)
from random import randint
cpu = randint(0, 10)
print('Vou pensar em um numero entre 0 e 10, tente advinhar: ')
print('-=-'*25)
n = int(input('Em que numero eu pensei?'))
t = 1
while n != cpu:
    n = int(input('Tente novamente, em que numero eu pensei? '))
    t += 1
    if n < cpu:
        print('Mais')
    if n > cpu:
        print('Menos')
from time import sleep
print('Processando...')
sleep(3)
if n == cpu:
    print('Parabens! Voce acertou, voce precisou de {} palpites'.format(t))
