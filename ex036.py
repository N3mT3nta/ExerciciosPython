from emoji import emojize
vcasa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o valor do seu salário: R$'))
anos = float(input('Em quantos anos você pretende pagar: '))
mensalidade = vcasa / (anos * 12)
if mensalidade < (salario * 1.30):
	print(
	    emojize(
	        'Parabéns! Seu empréstimo foi aprovado! A prestação será de R${:.2f} :satisfied:'
	        .format(mensalidade),
	        use_aliases=True))
else:
	print(
	    emojize(
	        'Infelizmente seu pedido de empréstimo foi negado. A prestação seria de R${:.2f} e excede 30% do seu salário :pensive:',
	        use_aliases=True))
