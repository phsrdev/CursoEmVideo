print('-=-'*10, 'Desafio 042', '-=-'*10)
print('-=-'*10, 'Desafio 035', '-=-'*10)
l1 = float(input('Primeiro segmento:'))
l2 = float(input('Segundo segmento:'))
l3 = float(input('Terceiro segmento:'))
if l1 < l2+l3 and l2 < l1+l3 and l3 < l2+l1:
    print('Os segmentos formam um triangulo ', end='')
    if l1 == l2 == l3:
        print('EQUILATERO.')
    elif l1 != l2 != l3 != l1:
        print('ESCALENO.')
    else:
        print('ISOSCELES.')
else:
    print('Os segmentos não formam um triangulo.')