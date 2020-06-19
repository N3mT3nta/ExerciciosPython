print('\033[1;31mSOMATÓRIO DE NÚMEROS PARES\033[m')
s = 0
for n in range(1, 7):
    num = int(input(f'Digite o {n}º valor: '))
    if num % 2 == 0:
      s = s + num
print(f'\033[1;32mA soma dos números pares é {s}')
