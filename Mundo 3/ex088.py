#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENAa criar
#palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6
#números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
print('{:^50}'.format(' Desafio 088 '))
from random import randint
from time import sleep
print('{:=^60}'.format(' GERADOR DE JOGOS MEGA SENA '))
cartao = []
while True:
    print()
    jogos = int(input('Quantos jogos voce quer criar? [0] PARA ENCERRAR '))
    if jogos == 0:
        break
    elif jogos >= 1:
        for l in range(1, jogos+1):
            for j in range(0, 6):
                j = randint(1, 60)
                while j in cartao:
                    cartao.pop
                    j = randint(1, 60)

                cartao.append(j)
            print(f'Criando seu {l}° jogo : ')
            sleep(1)
            print(f'Jogo: {sorted(cartao)}', end='')
            sleep(1)
            print()
            cartao.clear()
print('Boa sorte!')