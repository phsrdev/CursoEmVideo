print('-'*15, 'Desafio 014', '-'*15)
#Formula (1 °C × 9/5) + 32 = 33,8 °F
cel = float(input('Me diga qual a temperatura em celsius nesse momento?\n'))
f =  cel*(9/5)+32
print('Convertendo a temperatura {}°C, teremos {:.2f}°F'.format(cel, f))
