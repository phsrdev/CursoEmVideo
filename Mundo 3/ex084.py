#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
print('{:=^50}'.format(' Desafio 084 '))
pessoas = []
data = []
menor = maior = tot = 0
while True:
    nome = str(input('O nome: '))
    peso = float(input('O peso: '))
    opção = ' '
    if len(pessoas) == 0:
        maior += peso
        menor += peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
    data.append(nome)
    data.append(peso)
    pessoas.append(data[:])
    data.clear()
    tot += 1
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if opção in 'N':
        print(f'Foram cadastradas {tot} pessoas. ')
        break
print(f'Foram cadastradas {tot} pessoas.')
print(f'O maior peso foi: {maior}', end='')
for p in pessoas:
    if p[1] == maior:
        print(f' {p[0]} ', end='')
print(f'O menor peso foi: {menor}', end='')
for p in pessoas:
    if p[1] == menor:
        print(f' {p[0]} ', end='')




