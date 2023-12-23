print('Digite quatro valores:')

numeros = int(input()), int(input()), int(input()), int(input())
pares = []

for posicao, item in enumerate(numeros):
    if numeros[posicao] % 2 == 0:
        pares.append(item)

print(f'''
Os valores digitados foram: {numeros}

{f'O valor 9 aparece {numeros.count(9)} vez(es)' if numeros.count(
    9) != 0 else 'O valor 9 não aparece'}

{f'O valor 3 aparece pela primeira vez na posição {numeros.index(3) + 1}' if 3 in numeros else 'O valor 3 não aparece'}

{f'O(s) valor(es) par(es) é(são): {pares}' if pares != [
] else 'Não há valores pares'}
''')