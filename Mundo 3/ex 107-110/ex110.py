# Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada
# resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado
# até aqui.
import moeda

print(f'{" Desafio 110 ":=^50}')

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

moeda.resumo(numero)