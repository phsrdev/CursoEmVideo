print('-='*15, 'Desafio 064', '=-'*15)
n = int(input('Digite um numero: [999] Para encerrar o programa. '))
s = n - 999
c = 1
while n != 999:
    n = int(input('Digite um numero: [999] Para encerrar o programa. '))
    s += n
    if n != 999:
        c += 1
print('A soma dos {} numeros foi de: {}'.format(c, s))

