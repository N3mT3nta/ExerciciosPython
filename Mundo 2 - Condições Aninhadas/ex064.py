n = 0
total = 0
tentativas = 0

print('Digite qualquer valor diferente de 999 ou digite 999 para sair.\n')

while n != 999:
    n = int(input('Digite um número: '))
    total += n
    tentativas += 1

soma  = total - 999
print(f'\nVocê digitou {tentativas - 1} valores. A soma entre eles é {soma}.')
