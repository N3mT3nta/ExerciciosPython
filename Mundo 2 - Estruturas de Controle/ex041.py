from datetime import date
from time import sleep
idade = date.today().year - int(input('Em que ano você nasceu: ')) #idade == ano atual - ano de nascimento
print('Analisando dados...')
sleep(1)
print('Determinando sua categoria...')
sleep(2)
if idade <= 9:
    print('Você tem {} anos \nCategoria: MIRIM'.format(idade))
elif idade <= 14:
    print('Você tem {} anos \nCategoria: INFANTIL'.format(idade))
elif idade <= 19:
    print('Você tem {} anos \nCategoria: JÚNIOR'.format(idade))
elif idade <= 25:
    print('Você tem {} anos \nCategoria: SÊNIOR'.format(idade))
else:
    print('Você tem {} anos \nCategoria: MASTER'.format(idade))
