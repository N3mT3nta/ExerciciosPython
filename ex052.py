tot = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1):
	if num % c == 0:
		print('\033[32m')
		tot = tot + 1
	else:
		print('\033[31m')
	print('{} '.format(c), end=' ')
print(f'\033[mO valor {num} foi divisível {tot} vezes, portanto: ')
if tot == 2:
	print('\033[32mÉ primo')
else:
	print('\033[31mNão é primo')
