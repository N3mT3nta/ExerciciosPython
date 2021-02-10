from random import randint

rodadas = 0
usuario = num_usuario = ''

while True:
    while usuario != 'P' and usuario != 'I':
        usuario = input('Par ou Ímpar (P/I): ').upper()

    while type(num_usuario) != int:
        num_usuario = input('Seu número: ')

        if num_usuario.isdigit():
            num_usuario = int(num_usuario)

    num_computador = randint(1, 10)

    print(f'A escolha do computador foi {num_computador}')

    if (num_usuario + num_computador) % 2 == 0:
        resultado_da_soma = 'P'
        print('Resultado: PAR')
    else:
        resultado_da_soma = 'I'
        print('Resultado: ÍMPAR')

    if usuario == 'P':
        computador = 'I'
    else:
        computador = 'P'

    if resultado_da_soma != usuario:
        break

    print('\033[32mVocê ganhou a rodada!\033[m')

    rodadas += 1
    usuario = num_usuario = ''

print('\033[31mVocê perdeu a rodada :<\033[m')

print(f'Você ganhou {rodadas} rodadas')
