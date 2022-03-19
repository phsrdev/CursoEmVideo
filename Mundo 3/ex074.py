print('{:=^50}'.format(' Desafio 074 '))
from random import randint
cpu = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Eu sorteei os numeros: {cpu}')
print(f'O maior valor sorteado foi: {max(cpu)}')
print(f'O menor valor sorteado foi: {min(cpu)}')
