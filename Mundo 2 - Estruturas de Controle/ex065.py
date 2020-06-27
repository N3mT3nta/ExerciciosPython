maior = 0
menor = 0
continuar = 'S'
soma = 0
c = 0

while continuar == 'S':
    num = int(input('Digite um número: '))
    soma += num
    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    c += 1

    if num > maior:
        maior = num
    if c == 1:
        menor = num
    if num < menor:
        menor = num

media = soma / c

print(f'''
Você digitou {c} números
A média é {media}
O maior valor foi {maior}
O menor valor foi {menor}''')
