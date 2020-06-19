#While

num = int(input('Digite um número: '))
multiplicador = num - 1
fatorial = num
numx = 0
while multiplicador != 0:
    fatorial = (fatorial * multiplicador)
    multiplicador = multiplicador -1

print(f'{num}! = {fatorial}')

#Fast Mode

'''from math import factorial
num = int(input('Digite um número: '))
print(factorial(num))'''



#Usando o for

'''num = int(input('Digite um número: '))
nums = []
resultado = 0

for c in range(num, 0, -1):
    print(c)
    while c > 1:
        nums = '' + str(c)
    resultado = resultado * c
print(f'{num}x{nums} = {resultado}')'''
