dias = int(input('Quantos dias alugados: '))
km = float(input('Quantos Km percorridos:'))
t = (dias * 60) + (km * 0.15)
print(f'O valor total é de R${t:.2f}')
