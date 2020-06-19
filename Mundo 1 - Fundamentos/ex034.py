sal = float(input('Qual o valor do salário: R$'))
if sal > 1250:
  print('Você terá um aumento de 10% e receberá R${:.2f}'.format(sal*1.10))
if sal <= 1250:
  print('Você terá um aumento de 15% e receberá R${:.2f}'.format(sal*1.15))
