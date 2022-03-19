print('='*15, 'Desafio 069', '='*15)
cid = thom = tmum = 0
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    if idade > 18:
        cid += 1
    sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if sexo == 'M':
        thom += 1
    if sexo == 'F':
         if idade < 20:
             tmum += 1
    cont = input('Deseja cadastrar mais alguem? [S/N]').strip().upper()[0]
    if cont == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {cid}.')
print(f'Ao todo temos {thom} homens cadastrados.')
print(f'Temos {tmum} mulher com menos de 20 anos.')
