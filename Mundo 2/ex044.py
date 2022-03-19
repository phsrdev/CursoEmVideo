print('-=-'*10, 'Desafio 044', '-=-'*10)
compras = float(input('Qual o valor total de suas compras? \nR$'))
pag = int(input('Qual a forma de pagamento?\nA VISTA (DINHEIRO/CHEQUE) [1]\nA Vista no cartão [2]\nAté 2x no cartão [3]\n3x ou mais no cartão [4]\n'))
din = compras * 0.9
car = compras * 0.95
par = compras / 2
if pag == 1:
    print('Para pagamentos a vista, oferecemos 10% de desconto.\nO preço da sua compra passa a ser de: R${:.2f}'.format(din))
elif pag == 2:
    print('Para pagamentos a vista no cartão oferecemos 5% de desconto.\nO preço da sua compra passa a ser de R${:.2f}'.format(car))
elif pag == 3:
    print('O preço de sua compra foi de R${}.\nE sua parcela dividindo em 2x será de R${:.2f}.'.format(compras, par))
elif pag == 4:
    parcelas = int(input('Você gostaria de dividir em quantas parcelas?'))
    prest = (compras*1.2) / parcelas
    print('O preço de sua compra foi de R${} e o preco de sua parcela dividindo em {} vezes é de R${}.'.format(compras, parcelas, prest))
    print('Para mais do que 3 parcelas cobramos 20% de juros nas suas compras.\nSeu valor inicial de R${} com juros passa a ser de R${}'.format(compras, compras*1.2))
else:
    print('Não identifiquei o modo de pagamento, tente novamente.')

