dias = int(input('Por quantos dias o carro foi alugado?'))
km = float(input('Quantos Km rodados?'))
total = (60*dias)+(0.15*km)
print('O gasto total é de R${:.2f}'.format(total))
