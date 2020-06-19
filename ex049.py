from time import sleep
print('\033[1;31m-=' * 20)
print('\033[1;32m{:^40}'.format('TABUADA'))
print('\033[1;31m-=\033[m' * 20)
num = int(input('\033[33mDigite um número para ver sua tabuada: '))
print('\033[1;34mGerando resultados...')
sleep(2)
for n in range(1, 11):
	print('\033[1;36m{} x{:2} = {}'.format(num, n, num * n))
