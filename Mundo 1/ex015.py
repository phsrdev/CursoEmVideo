print('-'*15, 'Desafio 015', '-'*15)
dia = int(input('Quantos dias voce ficou com o carro?\n'))
km = float(input('Quantos quilometros voce andou com o carro nesse periodo?\n'))
valor = dia * 60 + km * 0.15
print('Você tem que pagar R${:.2f}, pelos {} dias alugados e {}km percorridos.'.format(valor, dia, km))
