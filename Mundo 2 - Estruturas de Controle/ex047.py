'''print('Mostrarei os números pares ou ímpares entre o intervalo que desejar.') #Tentativa de dar escolha ao usuário
num1 = int(input('Número de início: '))
num2  = int(input('Número de término: '))
print('Números pares entre {} e {}: '.format(num1, num2))'''

for lista in range(2, 51, 2):
	print(f'{lista}', end=' ')
print('\033[1;32mFIM')
