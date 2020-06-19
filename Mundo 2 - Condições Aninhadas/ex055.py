peso = 0
pesos = []

for c in range(1,6):
	peso = float(input(f'Peso da {c}º pessoa: '))
	pesos.append(peso)

print(f'O maior peso foi {max(pesos)}Kg')
print(f'O menor peso foi {min(pesos)}Kg')
