print('-=-'*10, 'Desafio 040', '-=-'*10)
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) /2
print('Tirando {:.1f} e {:.1f} sua media e de {}.'.format(nota1, nota2, media))
if 7 > media >= 5:
    print('O aluno ficou de RECUPERAÇÃO.')
elif media <= 4.99:
    print('O aluno esta REPROVADO.')
else:
    print('O aluno esta APROVADO.')

