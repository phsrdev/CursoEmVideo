print('-=-'*15, 'Desafio036', '-=-'*15)
valor = float(input('Digite o valor do imovel:\nR$'))
sal = float(input('Agora me diga o valor do salario do comprador:\nR$'))
anos = int(input('Agora me diga em quantos anos esse imovel sera financiado:\n'))*12
prest = valor / anos
if prest / sal <0.3:
    print('Credito aprovado, e a prestação do seu imovel sera de: R${:.2f}'.format(prest))
else:
    print('Credito negado.')