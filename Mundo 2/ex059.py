print('-='*15, 'Desafio 059', '-='*15)
opção = 0
n1 = int(input('Digite o 1° valor: '))
n2 = int(input('Digite o 2° valor: '))
while opção != 5:

    opção = int(input('''O que voce quer fazer com esses valores?
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos numeros
[5] Sair do programa
========== Qual é a sua opção? =========\n'''))
    if opção == 1:
        soma = n1+n2
        print('A soma de {} e {} é: {}'.format(n1, n2, soma))
    elif opção == 2:
        multi = n1 * n2
        print('A multiplicação de {} e {} é: {}'.format(n1, n2, multi))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        if n1 < n2:
            maior = n2
        print('O maior numero entre {} e {} é: {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Apagando da memoria... OK!!!')
        n1 = int(input('Digite o 1° valor: '))
        n2 = int(input('Digite o 2° valor: '))
    else:
        print('Opção invalida, tente novamente.')
    print('='*30)
print('Fim do programa, volte sempre!')

