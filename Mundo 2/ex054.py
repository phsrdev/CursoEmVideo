print('-='*15, 'Desafio 054', '-='*15)
from datetime import date
data = date.today().year
totmenor = 0
totmaior = 0
for pess in range(1, 8):
    nasc = int(input('Digite o ano em que a pessoa nasceu? '))
    idade = data - nasc
    if idade >= 21:

        totmaior +=1
    else:

        totmenor +=1
print('Temos {} maiores de idade.'.format(totmaior))
print('Temos {} menores de idade.'.format(totmenor))
