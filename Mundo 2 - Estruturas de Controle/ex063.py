num = int(input('Quantos números da sequência de Fibonacci você quer ver: '))
termo1 = 0
termo2 = 1
termo3 = 0
contador = 2

print(f'{termo1} → {termo2} → ', end='')

while contador != num:
    termo3 = termo1 + termo2

    print(termo3, end=' → ')

    termo1 = termo2
    termo2 = termo3
    contador += 1

print('FIM')
