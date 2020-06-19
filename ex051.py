pt = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
pa = 0
print('Mostrando os 10 primeiros termos da PA inserida:')
for c in range(1, 11):
	print(f'{pt}', end=' → ')
	pt = pt + razão
print('FIM')