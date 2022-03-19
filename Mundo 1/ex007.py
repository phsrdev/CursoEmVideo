print('Desafio 007')
aluno = str(input('Digite no nome do aluno:'))
mat = float(input('Digite a nota de matematica de {}:'.format(aluno)))
por = float(input('Digite a nota de portugues de {}:'.format(aluno)))
med = (mat+por)/2
print('A media de {} é de {}.'.format(aluno, med))