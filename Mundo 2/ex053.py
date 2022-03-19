print('-='*15, 'Desafio 053', '-='*15)
texto = str(input('Digite uma frase: ')).strip().upper()
palavras = texto.split()
junto = ''.join(palavras)
inverso = ''
#inverso = [::-1]
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if junto == inverso:
    print('Temos um palíndromo!')
else:
    print('Você digitou {} e invertido voce tem:\n {}'.format(junto, inverso))
