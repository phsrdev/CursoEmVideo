print('-'*15, 'Desafio 022', '-'*15)
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiusculas é: {}'.format(nome.upper()))
print('Seu nome em minusculas é: {}'.format(nome.lower()))
print('Seu nome completo possui: {} letras.'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele possui {} letras'.format(separa[0], len(separa[0])))
