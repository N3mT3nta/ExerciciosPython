valor = int(input('Valor à ser sacado: R$'))
notas_de_100 = valor // 100
valor_restante = valor % 100
notas_de_50 = valor // 50
valor_restante = valor % 50
notas_de_20 = valor_restante // 20
valor_restante = valor_restante % 20
notas_de_10 = valor_restante // 10
valor_restante = valor_restante % 10
notas_de_5 = valor_restante // 5
valor_restante = valor_restante % 5
notas_de_2 = valor_restante // 2
valor_restante = valor_restante % 2
notas_de_1 = valor_restante // 1

if notas_de_50 != 0:
    print(f'Notas de R$50: {notas_de_50}')

if notas_de_20 != 0:
    print(f'Notas de R$20: {notas_de_20}')

if notas_de_10 != 0:
    print(f'Notas de R$10: {notas_de_10}')

if notas_de_5 != 0:
    print(f'Notas de R$5: {notas_de_5}')

if notas_de_2 != 0:
    print(f'Notas de R$2: {notas_de_2}')

if notas_de_1 != 0:
    print(f'Notas de R$1: {notas_de_1}')

#Tentativa de uso do if inline

'''print(f'Notas de R$50: {notas_de_50}' if notas_de_50 != 0)

print(f'Notas de R$20: {notas_de_20}' if notas_de_20 != 0)

print(f'Notas de R$10: {notas_de_10}' if notas_de_10 != 0)

print(f'Notas de R$5: {notas_de_5}' if notas_de_5 != 0)

print(f'Notas de R$2: {notas_de_2}' if notas_de_2 != 0)

print(f'Notas de R$1: {notas_de_1}' if notas_de_2 != 0)'''

#Versão básica:

'''valor = int(input('Valor à ser sacado: R$'))
notas_de_50 = valor // 50
valor_restante = valor % 50
notas_de_20 = valor_restante // 20
valor_restante = valor_restante % 20
notas_de_10 = valor_restante // 10
valor_restante = valor_restante % 10
notas_de_1 = valor_restante

if notas_de_50 != 0:
    print(f'Notas de R$50: {notas_de_50}')

if notas_de_20 != 0:
    print(f'Notas de R$20: {notas_de_20}')

if notas_de_10 != 0:
    print(f'Notas de R$10: {notas_de_10}')

if notas_de_1 != 0:
    print(f'Notas de R$1: {notas_de_1}')'''