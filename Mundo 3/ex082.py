print('{:=^50}'.format(' Desafio 082'))
lista = []
par = []
impar = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    elif n % 2 != 0:
        impar.append(n)
    opção = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if opção in 'N':
        break
print(f'A sua lista de números completos foi: {lista}')
print(f'Os numeros pares são: {par}')
print(f'Os numeros impares são: {impar}')
print('Programa finalizado!')
