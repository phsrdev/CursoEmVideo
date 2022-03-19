print('{:=^50}'.format(' Desafio 072 '))

from random import randint
lista = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro',
         'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
         'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
         'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
         'Dezenove', 'Vinte')

for c in lista:
    jogador = 0
    jogador = int(input('Digite um numero entre 0 e 20: '))
    if jogador >20:
        jogador = int(input('Digite um numero entre 0 e 20: '))
    print(f'Você digitou o numero {lista[jogador]}')
    escolha = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    while escolha not in 'SN':
        escolha = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    if escolha == 'N':
        break
print('Programa finalizado!')