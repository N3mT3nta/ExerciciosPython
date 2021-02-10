mais_de_mil = total = 0
produto_mais_barato = continuar = produto = preço_mais_barato = preço = ''


while True:
    while produto == '':
        produto = input('Nome do produto: ')

    while not preço.isnumeric():
        preço = input('Preço: R$')

    preço = float(preço)

    if preço > 1000:
        mais_de_mil += 1

    if preço_mais_barato == '':
        produto_mais_barato = produto
        preço_mais_barato = preço
    
    if preço < preço_mais_barato:
        produto_mais_barato = produto
        preço_mais_barato = preço
    
    total += preço

    while continuar != 'S' and continuar != 'N':
        continuar = input('Continuar? [S/N]: ').strip().upper()

    if continuar == 'N':
        break
    
    continuar = produto = preço = ''

print(f'''
Total: R${total}
Produto mais barato: {produto_mais_barato}
Preço do produto mais barato: R${preço_mais_barato}
Produtos acima de R$1000: {mais_de_mil}
''')