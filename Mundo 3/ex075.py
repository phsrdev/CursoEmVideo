print('{:=^50}'.format(' Desafio 075 '))
n1 = (int(input('Digite um valor: ')),
      int(input('Digite um segundo valor: ')),
      int(input('Digite o terceiro valor: ')),
      int(input('Digite o ultimo valor: ')))
print(f'Você digitou os valores {n1}')
print(f'O valor 9 apareceu {n1.count(9)} vezes.')
if 3 in n1:
    print(f'O valor 3 apareceu na {n1.index(3)+1}° posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram ', end='')
for n in n1:
    if n % 2 == 0:
        print(n, end=' ')
print('FIM')
