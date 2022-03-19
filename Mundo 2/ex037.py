print('-=-'*15, 'Desafio 037', '-=-'*15)
num = int(input('Digite um numero: '))
bin = bin(num)
hex = hex(num)
oct = oct(num)
print('Você gostaria de converter o numero para:\n1 BINARIO\n2 OCTODECIMAL\n3 HEXADECIMAL')
opcao = int(input(''))
if opcao == 1:
    print('O numero {}, convertido para binario vira: {}'.format(num, bin[2:]))
elif opcao == 2:
    print('O numero {}, convertido para octadecimal vira: {}'.format(num, oct[2:]))
elif opcao == 3:
    print('O numero {}, convertido para hexadecimal vira: {}'.format(num, hex[2:]))
else:
    print('Opção invalida')
