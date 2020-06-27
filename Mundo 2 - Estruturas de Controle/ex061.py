#Aprimoramento do ex051

ptermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
c = 1

while c < 11:
    print(ptermo, end='')

    if c < 10:
        print(' → ', end='')

    c += 1
    ptermo += razao
