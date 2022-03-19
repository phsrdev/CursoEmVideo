def aumentar(n=0, p=0, formato=False):
    n = n + (n * p/100)
    return n if formato is False else moeda(n)


def diminuir(n=0, p=0, formato=False):
    n = n + (n * p/100)
    return n if formato is False else moeda(n)


def dobro(n=0, formato=False):
    n = n * 2
    return n if formato is False else moeda(n)


def metade(n=0, formato=False):
    n = n / 2
    return n if formato is False else moeda(n)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n}'.replace('.', '.')


def teste(n):
    try:
        float(n)
        n = float(n)
        return True
    except ValueError:
        return False


def resumo(n=0, taxa=10, taxr=5):
    print('-' * 30)
    print('Resumo do valor'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{taxa}% de aumento: \t{aumentar(n, taxa, True)}')
    print(f'{taxr}% de redução: \t{diminuir(n, taxr, True)}')
    print('-' * 30)

