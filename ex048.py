s = 0
cont = 0
for num in range(1, 501, 2):
	if num % 3 == 0:
		cont = cont + 1
		s = (s + num)
print('O somatório dos {} números é: \033[1;32m{}'.format(cont, s))
