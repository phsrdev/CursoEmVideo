print('-='*15, 'Desafio 060', '-='*15)
'''from math import factorial
n1 = int(input('Digite um numero para calcular seu fatorial: '))
fac = factorial(n1)
print('O fatorial de {} é: {}'.format(n1, fac))'''
#python com mudulos
n = int(input('Digite um numero para calcular seu fatorial: '))
c = n
f = 1
while c > 0:
    print('{} '.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)
