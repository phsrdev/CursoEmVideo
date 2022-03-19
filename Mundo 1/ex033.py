print('-=-'*10, 'Desafio 033', '-=-'*10)
n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero:'))
n3 = int(input('Terceiro numero:'))
menor = n1
if n2<n1 and n2<=n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('Analizando, {}, {}, {}\nPROCESSANDO...'.format(n1, n2, n3))
from time import sleep
sleep(3)
print('O menor valor é o {} e o maior valor e o {}'.format(menor, maior))


