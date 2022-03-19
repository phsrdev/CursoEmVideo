print('-='*15, 'Desafio 061', '-='*15)
print('='*10, 'Calculador de Progressão Aritimetica', '='*10)
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
t = n
c = 1
while c <= 10:
    print('{} → '.format(t), end= '')
    t += r
    c += 1
print('FIM')