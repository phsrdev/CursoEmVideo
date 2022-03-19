print('-'*15, 'Desafio 010', '-'*15)
brl = float(input('Quanto você possui em na sua carteira?\nR$'))
usd = brl/5.68
eur = brl/6.43
print('Com R${} você consegue comprar hoje:\nUS ${:.2f}\nEuro ${:.2f}'.format(brl, usd, eur))
print('-'*43)
