valores = []
pares = []
impares = []

while True:
    valores.append(int(input('Digite um valor: ')))
    if not input('Digite S para continuar: ') in 'Ss':
        break

for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print(f'''
Os valores digitados são {valores}
Os valores pares são {pares}
Os valores ímpares são {impares}
''')
