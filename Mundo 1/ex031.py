print('-=-'*10, 'Desafio 031', '-=-'*10)
dist = float(input('Qual a distancia da sua viagem em km? '))
from time import sleep
if dist <= 200:
    preço = dist * 0.50
    print('O preço da sua viagem é de:\nPROCESSANDO...')
    sleep(3)
    print('R${:.2f}'.format(preço))
else:
    preço = dist * 0.45
    print('O preço da sua viagem é de:\nPROCESSANDO...')
    sleep(3)
    print('R${:.2f}'.format(preço))