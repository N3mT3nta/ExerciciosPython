valores = []

while True:
    valores.append(int(input('Digite um valor: ')))
    if not input('Digite S para continuar: ') in 'Ss':
        break

valores.sort(reverse=True)

print(f'Vocẽ digitou {len(valores)} valores.')
print(f'Os valores em ordem decrescente são {valores}')

if 5 in valores:
    print('O valor 5 foi digitado.')
else:
    print('O valor 5 não foi digitado.')