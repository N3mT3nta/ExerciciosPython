from random import randint

rodadas = 0

while True:
    usuario = input('Par ou Ímpar (P/I): ').upper()

    '''if usuario != 'P' or usuario != 'I':
        print('Resposta inválida, tente novamente.')
        break'''

    num_usuario = int(input('Seu número: '))
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

print('\033[31mVocê perdeu a rodada :<\033[m')

print(f'Você ganhou {rodadas} rodadas')
