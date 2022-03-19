print('-=-'*10, 'Desafio 029', '-=-'*10)
vel = float(input('Seu veiculo esta andando a que velocidade? '))
mul = (vel - 80)*7
from time import sleep
if vel > 80:
    print('Você esta acima do limite de velocidade e por isso vai ser multado!\nProcessando...')
    sleep(2)
    print('O valor da sua multa é de R${}'.format(mul))
else:
    print('Ok, você esta dentro de limite de 80Km/h, pode seguier sua viagem')

