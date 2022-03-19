print('-=-'*10, 'Desafio 038', '-=-'*10)
nu1 = int(input('Me diga 2 numeros que e eu irei comparar eles:\nPrimeiro Numero: '))
nu2 = int(input('Segundo Numero: '))
if nu1 > nu2:
    print('O primeiro é maior que o segundo.')
elif nu1 < nu2:
    print('O segundo é maior que o primeiro.')
elif nu1 == nu2:
    print('Os dois numeros são iguais.')
else:
    print('Não consegui comparar os numeros, desculpe.')