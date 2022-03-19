#Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo
#que o vencedor tirou o maior número no dado.
print('{:-^90}'.format(' Desafio 090 '))
from random import randint
from time import sleep
dados = {}
dados['jog1'] = randint(1, 6)
dados['jog2'] = randint(1, 6)
dados['jog3'] = randint(1, 6)
dados['jog4'] = randint(1, 6)
print('ROLANDO DADOS')
print(f'Jogador 1 rolou: {dados["jog1"]}')
sleep(1)
print(f'Jogador 2 rolou: {dados["jog2"]}')
sleep(1)
print(f'Jogador 3 rolou: {dados["jog3"]}')
sleep(1)
print(f'Jogador 4 rolou: {dados["jog4"]}')
sleep(1)
print('{:=^90}'.format(' Rankeando os Jogadores '))
