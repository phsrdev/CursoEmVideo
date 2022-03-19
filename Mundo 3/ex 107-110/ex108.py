import moeda

# Exercício Python 108. Adapte o código do desafio #107, criando uma função adicional chamada moeda()
# que consiga mostrar os números como um valor monetário formatado.

print(f'{" Desafio 108 ":=^50}')

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

print(f'O dobro de R${numero} é R${moeda.moeda(moeda.dobro(numero))}')
print(f'A metade de R${numero} é R${moeda.moeda(moeda.metade(numero))}')
print(f'Aumentando 10%, temos R${moeda.moeda(moeda.aumentar(numero, 10))}')
