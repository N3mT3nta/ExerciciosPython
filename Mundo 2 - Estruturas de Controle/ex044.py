preço = float(input('Qual o preço do produto: R$'))
print('Digite o número referente ao método de pagamento desejado:')
print('1 - À vista em dinheiro ou cheque (10% de desconto)')
from time import sleep
print('2 - À vista no cartão (5% de desconto)')
print('3 - 2x no cartão (preço integral)')
print('4 - 3x ou mais no cartão (20% de juros)')
mpag = int(input('Opção desejada: '))
print('Calculando...')
sleep(2)
if mpag == 1:
    preçof = preço * 0.9
    print(
        'O preço original é de R${} \nO valor a ser pago é de R${:.2f}'.format(
            preço, preçof))
elif mpag == 2:
    preçof = preço * 0.95
    print(
        'O preço original é de R${} \nO valor a ser pago é de R${:.2f}'.format(
            preço, preçof))
elif mpag == 3:
    preçof = preço
    print(
        'O preço original é de R${} \nO valor a ser pago é de R${} em 2x de R${:.2f}'
        .format(preço, preçof, preçof / 2))
elif mpag == 4:
    preçof = preço * 1.20
    parc = int(input('Em quantas parcelas deseja pagar: '))
    print('O preço original é de R${} \nO valor a ser pago é de R${} em {}x de R${:.2f}'.format(preço, preçof, parc, preçof / parc))
else:
    print('\033[1;31mOpção inválida, tente novamente.')
