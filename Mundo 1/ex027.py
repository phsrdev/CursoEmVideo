print('-'*15, 'Desafio 027', '-'*15)
nome = str(input('Digite seu nome completo: ').upper().strip())
cnome = nome.split()
print('Muito prazer em te conhecer\nSeu primeiro nome é: {}'.format(cnome[0].title()))
print('E seu ultimo nome é: {}'.format(cnome[len(cnome)-1].title()))

