#PROBLEMA: OS RESULTADOS NÃO SÃO MOSTRADOS CORRETAMENTE.

# 1 = Pedra
# 2 = Papel
# 3 = Tesoura

from time import sleep
from random import randint

resultado = ''
continuar = 'S'
vitórias = 0
derrotas = 0
empates = 0

while continuar == 'S':

    cpu = randint(1,3)

    player = int(input('''
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura

'''))

    if player == 1 and cpu == 3 or player == 2 and cpu == 1 or player == 3 and cpu == 2: #Casos em que o player ganha.
        resultado = '\033[32mVocê Ganhou!\033[m'
        vitórias = vitórias + 1

    elif player == 1 and cpu == 2 or player == 2 and cpu == 3 or player == 1 and cpu == 1: #Casos em que o player perde.
        resultado = '\033[31mVocê Perdeu!\033[m'
        derrotas = derrotas + 1

    elif player == cpu: #Casos em que o jogo empata.
        resultado = '\033[33mEmpate!\033[m'
        empates = empates + 1

    elif player != 1 and player != 2 and player != 3: #Casos em que a resposta é inválida.
        resultado = '\033[31mResposta inválida. Tente novamente.\033[m'

    if cpu == 1:
        jogadacpu = 'Pedra'

    elif cpu == 2:
        jogadacpu = 'Papel'

    elif cpu == 3:
        jogadacpu = 'Tesoura'

    print('\nJO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ\n')

    print(f'O computador jogou {jogadacpu}.\n')
    sleep(1)
    print(f'{resultado}\n')

    continuar = input('Digite S para continuar e qualquer outra tecla para sair: ').upper()

print(f'''
RESULTADOS:

\033[32mVitórias: {vitórias}
\033[31mDerrotas: {derrotas}
\033[33mEmpates:  {empates}
''')
print('\033[32mFoi bom jogar com você. Tenha um bom dia.')

#VERSÃO ORIGINAL:

'''from random import randint #Adcionar resposta ao digitar números diferentes de 1, 2 e 3
from time import sleep
print('—=' * 20)
print('{:^40}'.format('JOKENPO'))
print('—=' * 20)
print('\n1 - Pedra \n2 - Papel \n3 - Tesoura \n')
user = int(input('Digite o número referente a sua escolha: '))
cpu = randint(1, 3)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
if user == 1:
    jgd = 'PEDRA'
elif user == 2:
    jgd = 'PAPEL'
elif user == 3:
    jgd = 'TESOURA'
if cpu == 1:
    pc = 'PEDRA'
elif cpu == 2:
    pc = 'PAPEL'
elif cpu == 3:
    pc = 'TESOURA'
print('O PC escolheu {} e vocẽ escolheu {}'.format(pc, jgd))
if user == 1 and cpu == 3 or user == 2 and cpu == 1 or user == 3 and cpu == 2:
    print('\033[32mVocê ganhou!')
elif user == 3 and cpu == 1 or user == 1 and user == 2 or user == 2 and cpu == 3:
    print('\033[31mVocê perdeu! Hahaha')
elif user == cpu:
    print('Empate')'''
