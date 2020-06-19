frase = input('Digite uma frase: ').strip().lower()
vez = frase.count('a')
print(f'A letra A aparece {vez} vezes nesta frase.')
a1 = frase.find('a') + 1
a2 = frase.rfind('a') + 1
print(f'Primeira aparição de A na posição {a1}.')
print(f'Última aparição de A na posição {a2}')
