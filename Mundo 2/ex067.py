print('-='*15, 'Desafio 067', '=-'*15)
print('='*30)
print('Desafio da Tabuada')
print('~~'*15)
c = 0
while True:
    n1 = int(input('Digite um numero para ver sua tabuada: '))
    print('='*30)
    if n1 < 0:
        break
    for c in range(1, 11):
        print(f'A tabuada de {n1} é:')
        print(f'{n1} x {c} = {n1*c}')
    print('='*30)
print('Programa tabuada encerrado. Volte sempre!!!')

