#using while

from time import sleep

num = int(input('Digite um número para calcular seu fatorial: '))
multiplicador = num
fatorial = 1 #1 é o elemento neutro da multiplicação

print(f'Calculando {num}!')
sleep(1)

while multiplicador != 0:
    print(multiplicador, end='')
    print(' x ' if multiplicador > 1 else ' = ', end='')
    fatorial *= multiplicador
    multiplicador -= 1

print(f'{fatorial}')

#easy mode

'''from math import factorial
num = int(input('Digite um número: '))
print(f'{num}! = {factorial(num)}')'''



#using for

'''from time import sleep

num = int(input('Digite um número para calcular seu fatorial: '))
multiplicador = num
fatorial = 1

print(f'Calculando {num}!')
sleep(1)

for multiplicador in range(num, 0, -1):
    print(multiplicador, end='')
    print(' x ' if multiplicador > 1 else ' = ', end='')
    fatorial *= multiplicador
    multiplicador -= 1

print(f'{fatorial}')'''
