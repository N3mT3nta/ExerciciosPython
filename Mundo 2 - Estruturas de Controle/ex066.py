soma = 0
valores = 0

print('''Soma de valores

#Digite 999 para sair
''')

while True:
    num = int(input('Número: '))
    if num == 999:
        break
    soma += num
    valores += 1

print(f'A soma dos {valores} valores digitados é {soma}.')
