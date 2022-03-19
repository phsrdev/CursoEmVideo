# Exercício Python 109. Modifique as funções criadas no desafio 107 para elas aceitarem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), # # desenvolvida no
# desafio 108.
import moeda

print(f'{" Desafio 109 ":=^50}')

numero = str(input('Digite um preço: R$'))
while True:
    try:
        moeda.teste(numero)
        if True:
            numero = float(numero)
        break
    except:
        print(f'ERRO! {numero} é invalido.')
        numero = str(input('Digite um preço: R$'))

print(f'O dobro de {moeda.moeda(numero)} é R${moeda.dobro(numero, True)}')
print(f'A metade de {moeda.moeda(numero)} é R${moeda.metade(numero, True)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(numero, 10, True)}')
print(f'Reduzindo 13%, temos R${moeda.diminuir(numero, 13, True)}')
