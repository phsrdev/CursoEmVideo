print('{:=^50}'.format(' Desafio 079 '))
lista = []
while True:
    n = int(input('Digite um valor numerico: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado, não posso adicionar.')

    opção = str(input('Quer continuar? [S/N]:')).upper().strip()[0]
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N]:')).upper().strip()[0]
    if opção == 'N':
        break
print(f'Voce digitou os valores: {sorted(lista)}')
