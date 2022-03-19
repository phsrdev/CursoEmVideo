print('-=-'*10, 'Desafio 034', '-=-'*10)
sal = float(input('Qual o salario do funcionario? '))
if sal > 1250:
    sal = sal*1.10
else:
    sal = sal*1.15
print('Com o novo reajuste o salario do funcionario passa a ser:\nR${}'.format(sal))
