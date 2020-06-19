n1 = int(input('\033[34mDigite um número: '))
n2 = int(input('\033[35mDigite outro número: '))
s = n1+n2
print('\033[33mA soma entre {}{}{} e {}{}{} é {}{}'.format('\033[34m', n1, '\033[m', '\033[35m', n2, '\033[m', '\033[36m', s))
