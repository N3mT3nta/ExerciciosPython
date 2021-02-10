maiores = homens = mulheres_20 = 0
idade = genero = continuar = ''

while True:
    while not idade.isdigit():
        idade = input("Idade da pessoa: ")

    idade = int(idade)

    while genero != 'M' and genero != 'F':
        genero = input('Gênero da pessoa [M/F]: ').strip().upper()

    if idade >= 18:
        maiores += 1

    if genero == 'M':
        homens += 1

    if idade < 20 and genero == 'F':
        mulheres_20 += 1

    while continuar != 'S' and continuar != 'N':
        continuar = input('Deseja continuar? [S/N]: ').strip().upper()

    if continuar == 'N':
        break

    idade = ''
    genero = ''
    continuar = ''

print(f'''
Maiores de 18 anos: {maiores}
Homens: {homens}
Mulheres menores de 20 anos: {mulheres_20}
''')
