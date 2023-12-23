valores = []

for indice in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {indice}: ')))

maior = max(valores)
menor = min(valores)
pos_maior = []
pos_menor = []

for pos, valor in enumerate(valores):
    if maior == valor:
        pos_maior.append(pos)
    if menor == valor:
        pos_menor.append(pos)


print(f'''
Vocẽ digitou os valores {valores}
O maior valor digitado foi {max(valores)} nas posições {pos_maior}
O menor valor digitado foi {min(valores)} nas posições {pos_menor}''')
