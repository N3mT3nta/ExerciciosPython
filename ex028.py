#Aprimorado no ex058

from random import randint
from time import sleep
cpu = randint(0, 5)
user = int(input('Digite um número de 0 a 5: '))
print('Processando...')
sleep()
print(f'O computador escolheu {cpu}')
print('Você acertou, parabéns!' if user == cpu else f'Você errou! Tente novamente.')
