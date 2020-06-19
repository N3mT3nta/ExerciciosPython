r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('É possível formar um triângulo equilátero.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Você poderá formar um triângulo isósceles.')
    else:
        print('Você poderá formar um triângulo escaleno.')
else:
    print('As retas inseridas não formam um triângulo.')
