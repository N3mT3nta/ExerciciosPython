from random import randint

numeros = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)

print(f'Os valores sorteados foram: ', end='')

for c in range(0, len(numeros)):
    print(numeros[c], end=' ')

print(f'''
O maior valor sorteado foi {max(numeros)}
O menor valor sorteado foi {min(numeros)}
''')
