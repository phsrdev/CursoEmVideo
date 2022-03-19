print('-=-'*10, 'Desafio 043', '-=-'*10)
peso = float(input('Quanto voce pesa em kg? XXX.xx\n'))
altu = float(input('Qual sua altura em metros? X.xx\n'))
imc = peso / (altu*altu)
print('Pesando {} kgs e medindo {}M seu IMC e de {:.2f}.'.format(peso, altu, imc))
if imc <= 18.5:
    print('Você esta abaixo do seu peso ideal.')
elif imc <= 25:
    print('Você esta com seu peso ideal.')
elif imc <= 30:
    print('Você esta com sobrepeso.')
elif imc <= 40:
    print('Você esta obeso.')
else:
    print('Você esta com obesidade morbida.')



