print('-=-' * 10, 'Desafio 039', '-=-' * 10)
from datetime import date
sexo = input('Qual seu sexo? Masculino = 1 Feminino = 2: ')
ano = date.today().year
data = int(input('Estamos no ano {} em que ano você nasceu? '.format(ano)))
idade = ano - data
print('Você tem {} anos.'.format(idade))

if idade < 18:
    alist = (18 - idade)
    print('Você ainda vai se alistar. Ainda faltam {} anos até seu alistamento.'.format(alist))
    saldo = ano - idade
    print('Seu alistamento vai ser em {}'.format(saldo))
elif idade > 18:
    alist = ano - (idade - 18)
    print('Seu alistamento militar ja passou. Você se alistou em {}.'.format(alist))
    saldo = ano - idade
    print('Seu alistamento foi em {}'.format(saldo))
else:
    print('No Brasil, mulheres nao precisam se alistar, tenha um bom dia!')