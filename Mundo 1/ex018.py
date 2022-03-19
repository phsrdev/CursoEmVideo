import math
print('-'*15, 'Desafio 018', '-'*15)
ang = float(input('Digite um angulo: '))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
sin = math.sin(math.radians(ang))
print('O angulo de {:.2f}°\npossui como seno {:.2f}\nseu cosseno e {:.2f}\ne sua tangente é {:.2f}'.format(ang, sin, cos, tan))
