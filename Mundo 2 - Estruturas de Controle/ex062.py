num = int(input('1° Termo da PA: '))
razao = int(input('Razão da PA: '))
continuar = True
termos = int(input('N° de termos desejados: '))
total_de_termos = termos

while continuar == True:
    for c in range(1, termos + 1):
        print(f'{num}', end='')

        if c < termos:
            print(f' -> ', end='')

        num = num + razao

    continuar = input('''

Continuar?

[ 1 ]     Sim
[ Outro ] Não

''')

    if continuar == '1':
        termos = int(input('N° de novos termos: '))
        continuar = True
        total_de_termos += termos

    else:
        continuar = False

print(f'\n Programa finalizado, {total_de_termos} termos mostrados.')
