print('-='*15, 'Desafio 070', '=-'*15)
print('='*40)
print('{:^40}'.format('LOJA SUPER BARATAO'))
print('='*40)
nbar = ''
soma = caro = cont = 0
while True:
    prod = str(input('Nome do produto: ')).upper()
    cont += 1
    preço = float(input('Preço: R$ '))
    if cont == 1:
        bara = preço
        nbar = prod
    elif preço < bara:
        bara = preço
        nbar = prod
    soma += preço
    if preço >= 1000:
        caro += 1
    novo = ' '
    while novo not in 'SN':
        novo = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if novo == 'N':
        break
print('='*40)
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print('='*40)
print(f'Total de suas compras foi de: R${soma:.2f}.')
print(f'Na sua lista de comprar temos {caro} itens que custem mais de R$1000.00')
print(f'O produto mais barato é {nbar} que custou {bara}')
