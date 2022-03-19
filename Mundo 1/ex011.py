print('-'*15, 'Desafio 011', '-'*15)
alt = float(input('Qual a altura de sua parede em metros? (APENAS NUMEROS)\n'))
lar = float(input('Ok, agora qual a largura de sua parede?\n'))
area = alt*lar
tinta = area/2
print('Sua parede tem a dimensão de {} x {} e sua area é de: {}m²'.format(alt, lar, area))
print('Para pintar essa parede, você precisará de {:.3f}L de tinta.'.format(tinta))