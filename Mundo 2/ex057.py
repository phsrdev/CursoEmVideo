print('-='*15, 'Desafio 057', '-='*15)
sexo = str(input('Digite seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos, Por favor informe seu sexo! M ou F:  ')).upper().strip()[0]
print('Sexo {} registrado.'.format(sexo))

