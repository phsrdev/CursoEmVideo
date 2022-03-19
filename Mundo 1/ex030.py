print('-=-'*10, 'Desafio 030', '-=-'*10)
num = int(input('Me diga um numero: '))
from time import sleep
print('Analisando o numero {}'.format(num))
sleep(3)
res = num % 2
if res == 0:
    print('O numero {} é par.'.format(num))
else:
    print('O numero {} é impar.'.format(num))
