km = float(input('Qual a distância da viagem em Km: '))
if km <= 200:
  print('O custo é de R$0,50 por Km e o valor da passagem será de R${}'.format(km * 0.5))
else:
  print('O custo é de R$0,45 por Km e o valor da passagem será de R${}'.format(km * 0.45))
