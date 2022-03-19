print('-='*15, 'Desafio 050', '-='*15)
print('='*30)
print('10 TERMOS DE UMA PA')
print('='*30)
pa = int(input('Digite o 1° termo: '))
razao = int(input('Digite a RAZÃO: '))
decimo = pa + (10 - 1) * razao
for c in range((pa), decimo + razao , razao):
    print(c)
print('Acabou')
