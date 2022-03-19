print('-='*15, 'Desafio 068', '=-'*15)
from random import randint
cont = 0
while True:
    cpu = randint(0, 10)
    print('='*40)
    print('Vamos jogar PAR ou IMPAR')
    print('='*40)
    jogador = int(input('Digite um valor: '))
    opção = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    if opção in 'P':
        opção = 'PAR'
        ocpu = 'IMPAR'
    if opção in 'I':
        opção = 'IMPAR'
        ocpu = 'PAR'
    print('*'*40)
    resultado = jogador + cpu
    if resultado % 2 == 0:
        jogo = 'PAR'
    else:
        jogo = 'IMPAR'
    if jogo == opção:
        print('Você venceu!!! Parabens!!!')
        cont += 1
    else:
        print(f'GAME OVER!\nVocê perdeu, após {cont} vitorias.')
        break
    print(f'Você escolheu {jogador} e {opção}\nO computador escolheu {cpu} e {ocpu}  \n Deu {resultado} que é {jogo}')