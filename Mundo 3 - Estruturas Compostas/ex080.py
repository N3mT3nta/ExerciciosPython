valores = []

for c in range(1, 6):
    novo_valor = int(input('Digite um valor: '))

    if c == 1:
        valores.append(novo_valor)
        print('Valor adicionado ao começo da lista.')

    else:
        for pos, valor in enumerate(valores):
            if novo_valor < valor:
                valores.insert(pos, novo_valor)
                print(f'Valor adicionado na posição {pos} da lista.')
                break

            elif novo_valor == valor:
                valores.insert(pos, novo_valor)
                print(f'Valor adicionado na posição {pos} da lista.')
                break

            elif novo_valor > valor and valor == valores[-1]:
                valores.append(novo_valor)
                print('Valor adicionado ao final da lista.')
                break

print(f'''A lista digitada foi {valores}''')
