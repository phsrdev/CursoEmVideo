print('{:=^50}'.format(' Desafio 073 '))
brasileiro = ('Atletico-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthias',
              'Bragantino', 'Fluminense', 'America-MG', 'Atletico-GO', 'Santos',
              'Ceara SC', 'Internacional', 'Sao Paulo', 'Atletico-PR', 'Cuiaba',
              'Juventude', 'Gremio', 'Bahia', 'Sport Recife', 'Chapecoense')
print(f'Os 5 primeiros colocados do campeonato brasileiro de futebol serie A foram: {brasileiro[0: 5]}')
print(f'Os 4 ultimos colocados e por isso rebaixados para a serie B foram: {brasileiro[16:]}')
print(f'Os times que competiram em ordem alfaberica foram: {sorted(brasileiro)}')
print(f'A Chapecoense esta na {brasileiro.index("Chapecoense")+1}° posição')



