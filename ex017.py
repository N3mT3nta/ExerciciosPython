from math import hypot
print('Digite as medidas do triângulo retângulo:')
catop = float(input('Cateto oposto: '))
catad = float(input('Cateto adjacente: '))
hipot = hypot(catop, catad)
print(f'A hipotenusa de triângulo cujos catetos medem {catop} e {catad} equivale a {hipot:.2f}')
