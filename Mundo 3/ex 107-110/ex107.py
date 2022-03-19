import moeda

# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
# diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas
# funções.

print(f'{" Desafio 107 ":=^50}')

numero = str(input('Digite um preço: R$'))
while True:
    if numero.isnumeric():
        numero = float(numero)
        break
    else:
        print(f'ERRO! {numero} é invalido.')
        numero = str(input('Digite um preço: R$'))
print(f'O dobro de R${numero} é R${moeda.dobro(numero)}')
print(f'A metade de R${numero} é R${moeda.metade(numero)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(numero, 10)}')
