print('{:=^50}'.format(' Desafio 078 '))
lista = []
maior = menor = 0
for p in range(0, 5):
    lista.append(int(input(f'Digite um valor para posição {p}: ')))
    if p == 0:
        maior = lista[0]
        menor = lista[0]

    else:
        if lista[p] >= maior:
            maior = lista[p]
        if lista[p] <= menor:
            menor = lista[p]

print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posições: ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nar posições: ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')


