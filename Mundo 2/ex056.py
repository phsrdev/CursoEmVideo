print('-='*15, 'Desafio 056', '-='*15)
totidade = 0
homem = 0
mulher = 0
velho = 0
nomev = ''
mu20 = 0
for p in range(1, 5):
    print('='*5,'{} Pessoa'.format(p), '='*5)
    nome = str(input('Digite o nome: '))
    idade = int(input('Agora a idade: '))
    totidade += idade
    sexo = str(input('Sexo M/F? '.format(p))).upper()
    if p == 1 and sexo in 'Mm':
        velho = idade
        nomev = nome
    if sexo in 'Mm' and idade > velho:
        velho = idade
        nomev = nome
    if sexo in 'Ff' and idade < 20:
        mu20 += 1
print('A media de idade do grupo é de: {:.2f} anos.'.format(totidade/4))
print('O nome do homem mais velho é {} e ele tem {} anos.'.format(nomev, velho))
print('Temos no grupo {} mulheres com menos de 20 anos.'.format(mu20))
