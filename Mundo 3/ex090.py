#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando
#também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
print('{:-^50}'.format(' Desafio 090 '))
dados = {}
dados['nome'] = str(input('Nome do aluno: '))
dados['media'] = float(input(f'Media de {dados["nome"]}: '))
if dados['media'] >= 7:
    dados['resultado'] = 'APROVADO'
elif 5 <= dados['media'] < 7:
    dados['resultado'] = 'RECUPERAÇÃO'
elif dados['media'] < 5:
    dados['resultado'] = 'REPROVADO'
for k, v in dados.items():
    print(f' - {k} é igual a {v}')
