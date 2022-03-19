print('Desafio 008')
metro = float(input('Digite uma metragem:'))
mm = 1000*metro
cm = 100*metro
km = metro/1000
hm = metro/100
dm = metro*10
dam = metro/10
print('O valor em centimetro é de {:.0f}cm.\nDe decimetro é de {:.0f}dm.\nDe milimetros {:.0f}mm.'.format(cm, dm, mm))
print('Esse valor representa em quilometros de {}km.\nDe hectometro {}hm.\nDe decametro {}dam.'.format(km, hm, dam))


