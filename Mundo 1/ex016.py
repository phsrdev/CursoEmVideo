from math import trunc
print('-'*15, 'Desafio 015', '-'*15)
num = float(input('Digite um numero com (.)\n EX 1.234 : '))
res = trunc(num)
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, res))

