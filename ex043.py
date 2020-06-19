from time import sleep
peso = float(input('Quantos Kg você pesa: '))
altura = float(input('Qual a sua altura em metros: '))
imc = peso / (altura**2)
print('Analisando dados...')
sleep(1)
print('Seu IMC é {:.1f} e seu status é:'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
