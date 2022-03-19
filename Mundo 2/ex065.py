print('-='*15, 'Desafio 065', '=-'*15)
opção = 's'
cont = soma = 0
maior = 0

while opção != 'N':
    n1 = int(input('Digite um numero: '))
    cont += 1
    soma += n1
    menor = n1
    if n1 < menor:
        menor = n1
    if n1 > maior:
        maior = n1
    opção = str(input('Quer continuar? [S/N] ').strip().upper())[0]
media = soma / cont
print('Você digitou {} números e a media deles foi de: {:.2f}'.format(cont, media))
print('O maior deles foi {} e o menor deles foi {}.'.format(maior, menor))
