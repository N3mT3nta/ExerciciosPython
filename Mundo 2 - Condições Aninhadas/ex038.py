n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
if n1 > n2:
	print('O \033[1;31mprimeiro\033[m valor é maior')
elif n2 > n1:
	print('O \033[1;31msegundo\033[m valor é o maior')
else:
	print('\033[1;31mNão existe\033[m valor maior, os dois são iguais.')
