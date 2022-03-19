print('{:=^50}'.format(' Desafio 081 '))
#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista
lista = []
cont = 0
while True:
    n = int(input('Digite um valor para adicionar a lista: '))
    if n == 5:
        cont += 1
    lista.append(n)
    opção = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if opção in 'N':
        break
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} valores e eles foram: {lista}')
if 5 in lista:
    print(f'O valor 5 esta presente na lista.')
else:
    print(f'O valor 5 não esta presente na lista.')

