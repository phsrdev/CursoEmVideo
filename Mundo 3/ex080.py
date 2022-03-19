print('{:=^50}'.format(' Desafio 080 '))
#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os
# em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
lista = []
base = 0
for c in range(1, 6):
    n = int(input(f'Digite o {c} valor: '))
    if c == 1 or n > lista[len(lista)-1]:
        lista.append(n)
        base = n
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]
                lista.insert(pos, n)
                break
            pos += 1

print(lista)
