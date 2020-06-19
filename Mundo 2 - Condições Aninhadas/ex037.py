num = int(input('Digite o número inteiro que deseja converter:'))
conv = int(
    input(
        'Digite o número referente a base de conversão desejada: \n1 - Binário \n2 - Octal \n3 - Hexadecimal \n\nSua Opção:'
    ))
if conv == 1:
	numconv = bin(num)
	print('{} em binário: {}'.format(num, numconv[2:]))
elif conv == 2:
	numconv = oct(num)
	print('{} em octal: {}'.format(num, numconv[2:]))
elif conv == 3:
	numconv = hex(num)
	print('{} em hexagonal: {}'.format(num, numconv[2:]))
else:
	print('Opção inválida. Tente novamente.')
