from math import hypot
co = float(input('Cateto oposto:'))
ca = float(input('Cateto adjacente:'))
#h = (co**2 + ca**2) ** (1/2)
#print('O quadrado da hipotenusa deste triângulo vale {:.2f}'.format(h))
h = hypot(co, ca)
print('A hipotenusa desse triângulo vale {:.2f}'.format(h))
