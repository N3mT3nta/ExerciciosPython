#Aprimoramento do ex051

ptermo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
c = 1

print()

while c < 11:
    termos = razão * c
    print(f'{termos}', end=" → ")
    c += 1
print('FIM')

