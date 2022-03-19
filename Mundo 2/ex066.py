print('-='*15, 'Desafio 066', '-='*15)
cont = soma = 0
while True:
    n1 = int(input('Digite um valor (999 para parar): '))
    if n1 == 999:
        break
    cont += 1
    soma += n1
print(f'A soma dos {cont} valores foi {soma}!')
