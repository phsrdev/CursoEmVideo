print('-=-'*15, 'Desafio 035', '-=-'*15)
l1 = float(input('Primeiro segmento:'))
l2 = float(input('Segundo segmento:'))
l3 = float(input('Terceiro segmento:'))
if l1 < l2+l3 and l2 < l1+l3 and l3 < l2+l1:
    print('Os segmentos formam um triangulo')
else:
    print('Os segmento não formam um triangulo')
