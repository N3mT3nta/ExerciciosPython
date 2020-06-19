import forex_python.converter
c = float(input('Quantos reais vocễ tem em sua carteira: R$'))
dol = c / 4.10
euro = c / 4.52
print(f'\033[32mCom R${c} você pode comprar {dol:.2f} dólares ou {euro:.2f} euros.')
