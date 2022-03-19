print('-=-'*10, 'Desafio 041', '-=-'*10)
from datetime import date
ano = date.today().year
nasc = int(input('Digite o seu ano de nascimento: XXXX\n'))
idade = ano - nasc
if idade <= 9:
    print('Você tem {} anos e sua categoria é MIRIM.'.format(idade))
elif idade <= 14:
    print('Você tem {} anos e sua categoria é INFANTIL.'.format(idade))
elif idade <= 19:
    print('Você tem {} anos e sua categoria é JUNIOR.'.format(idade))
elif idade <= 25:
    print('Você tem {} anos e sua categoria é SENIOR.'.format(idade))
else:
    print('Você tem {} anos e sua categoria é MASTER.'.format(idade))
