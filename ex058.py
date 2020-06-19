#Aprimoramento do ex028

from random import randint
from time import sleep

user = -1
tentativas = 0
cpu = randint(0, 10)

while user != cpu:
    tentativas = tentativas + 1
    user = int(input('Digite um número de 0 a 10: '))
    print('Processando...\n')
    sleep(1)

    if user < cpu:
        print('\033[31mÉ mais. Tente novamente.\033[m\n')
    
    elif user > cpu:
        print('\033[31mÉ menos. Tente novamente.\033[m\n')

    elif tentativas == 1 :
        print('\033[32mVocê acertou de primeira, parabéns!')

    else:
        print(f'\033[4;32mParabéns, você acertou!'+ '\033[m ' + f'\033[4;31mMas foi em {tentativas} tentativas.')
