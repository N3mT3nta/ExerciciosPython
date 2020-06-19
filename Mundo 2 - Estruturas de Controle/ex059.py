from time import sleep

valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
sair = False

while sair == False:
    sleep(1)
    ação = int(
        input('''
O que deseja?

[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Redigitar
[ 5 ] Sair

'''))

    if ação == 1:
        print()
        print(f'A soma de {valor1} e {valor2} é {valor1 + valor2}')
        print()

    elif ação == 2:
        print()
        print(f'O produto {valor1} e {valor2} é {valor1 * valor2}')
        print()

    elif ação == 3:
        print()
        print(f'O maior valor digitado foi {max(valor1, valor2)}')
        print()

    elif ação == 4:
        print()
        valor1 = float(input('Primeiro valor: '))
        valor2 = float(input('Segundo valor: '))

    elif ação == 5:
        print()
        print('Saindo...')
        sleep(3)
        print('Tenha um bom dia!')
        sair = True

    else:
        print()
        print('\033[31mOpção inválida.\033[m')
        print()
