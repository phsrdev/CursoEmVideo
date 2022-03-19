print('-='*10, 'Desafio 070', '=-'*10)
print('='*50)
print('{:^50}'.format('Banco Pelfudo'))
print('='*50)
print('Nosso caixa possui cédulas de R$50, R$20, R$10 e R$1.\nNão é permitido o saque de ou deposito de moedas.')

while True:
    saque = int(input('Que valor você quer sacar? \nR$'))
    resp = ' '
    total = saque
    nota = 50
    tn = 0
    while True:
        if total >= nota:
            total -= nota
            tn += 1
        else:
            if tn > 0:
                print(f'Total de {tn} notas de R${nota}.')
            if nota == 50:
                nota = 20
            elif nota == 20:
                nota = 10
            elif nota == 10:
                nota = 1
            tn = 0
            if total == 0:
                break
    while resp not in 'SN':
        resp = str(input('Gostaria de realizar outra operação? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print('{:-^50}'.format(' FIM DO PROGRAMA '))
print('Obrigado pela preferencia! Volte sempre.')
