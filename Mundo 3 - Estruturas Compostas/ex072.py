nomes = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
         'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
         'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    numero = int(input('Digite um número entre 0 e 20: '))

    while True:
        if numero < 0 or numero > 20:
            numero = int(input('Tente novamente. Digite um número entre 0 e 20: '))
        else:
            break

    print(f'O número por extenso é: {nomes[numero]}')

    if input('Digite S para continuar, outra tecla para sair: ') not in 'Ss':
        break
