valores = []

while True:
    valor = int(input('Digite um valor: '))

    if valor in valores:
        print('Valor já adicionado. Insira outro.')
    else:
        valores.append(valor)
        print('Valor adicionado com sucesso.')

    if not input('Digite S para continuar: ') in 'Ss':
        break

valores.sort()

print(f'Os valores digitados e em ordem crescente são {valores}')
