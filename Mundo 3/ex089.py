# Exercício Python 089: crie um programa que leia nome e duas notas de vários alunos e guarde tudo numa
# lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário
# possa mostrar as notas de cada aluno individualmente.
print('{:=^60}'.format(' Desafio 089 '))
opc = ' '
ficha = []
alunos = []
while True:
    nome = str(input('Nome do aluno: '))
    n1 = float(input('Nota do 1° Trimestre: '))
    n2 = float(input('Nota do 2° Trimestre: '))
    n3 = float(input('Nota do 3° Trimestre: '))
    n4 = float(input('Nota do 4° Trimestre: '))
    media = (n1+n2+n3+n4) / 4
    ficha.append([nome, [n1, n2, n3, n4], media])
    alunos.append(ficha[:])
    opc = str(input('Deseja Continuar? [S/N]')).upper().strip()[0]
    while opc not in 'SN':
        opc = str(input('Deseja Continuar? [S/N]')).upper().strip()[0]
    if opc in 'N':
        break
print('*'*60)
print(f'{"No.":<4}{"Nome":<10}{"Media":>8}')
print('-'*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*30)
    opc = int(input('Mostrar notas de qual aluno? 999 PARA ENCERRAR '))
    if opc == 999:
        break
    if opc <= len(ficha)-1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}.')



