km = int(input(('Qual a velocidade do carro em Km/h: ')))
if km <=80:
  print('O motorista seguiu as leis de trânsito.')
else:
  print('O motorista estava acima da velocidade máxima permitida e sua multa será de R${}.'.format((km-80)*7))
