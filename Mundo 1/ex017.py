print('-'*15, 'Desafio 017','-'*15)
cat1 = float(input('Comprimento do cateto oposto: '))
cat2 = float(input('Comprimento do cateto adjacente: '))
hip = ((cat1 ** 2) + (cat2 ** 2))**(1/2)
print('A hipotenusa desse triangulo é {:.2f}'.format(hip))
from math import hypot
ca = float(input('Comprimento do cateto adjacente: '))
co = float(input('Comprimento do cateto oposto: '))
hi = hypot(co, ca)
print('A hipotenusa desse triangulo é {:.2f}'.format(hi))
