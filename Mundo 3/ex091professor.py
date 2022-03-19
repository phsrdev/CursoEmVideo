#Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo
#que o vencedor tirou o maior número no dado.
print('{:-^90}'.format(' Desafio 090 '))
from random import randint
from time import sleep
from operator import itemgetter
dados = {'Jogador 1': randint(1, 6),
         'Jogador 2': randint(1, 6),
         'Jogador 3': randint(1, 6),
         'Jogador 4': randint(1, 6)}
print('ROLANDO DADOS')
ranking = []
for k, v in dados.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print('{:=^90}'.format(' Rankeando os Jogadores '))
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}.')
    sleep(1)
