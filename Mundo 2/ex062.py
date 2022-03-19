print('-='*15, 'Desafio 062', '-='*15)
print('='*10, 'Calculador de Progressão Aritimetica', '='*10)
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
t = n
c = 1
o = -1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print('{} → '.format(t), end= '')
        t += r
        c += 1
    print('Pause')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progessão finalizada com {} termos mostrados.\nFim!!!'.format(total))
