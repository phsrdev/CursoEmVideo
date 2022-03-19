from time import sleep
from random import randint
print('-='*15, 'Desafio 045', '-='*15)
itens = ('Nulo', 'Pedra', 'Papel', 'Tesoura')
computador = randint (1, 3)
jogador = int(input('''Vamos jogar Jokenpô.
Suas opções são:
[1] Pedra
[2] Papel
[3] Tesoura
Qual voce deseja? '''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-='*30)
print ('Você escolheu {}'.format(itens[jogador]))
print('O computador escolheu {}'.format(itens[computador]))
print('-='*30)
if jogador == computador: # Pedra
    print('Ninguem ganhou, deu EMPATE.')
elif computador == 1:
    if jogador == 2: #
        print('Você venceu, Parabens!!!')
    elif jogador == 3:
        print('Você perdeu, boa sorte na proxima!')
elif computador == 2: # Papel
    if jogador == 3: #
        print('Você venceu, Parabens!!!')
    elif jogador == 1:
        print('Você perdeu, boa sorte na proxima!')
elif computador == 3: # Tesoura
    if jogador == 1: #
        print('Você venceu, Parabens!!!')
    elif jogador == 2:
        print('Você perdeu, boa sorte na proxima!')
