from datetime import date
ano = int(input('Em que ano você nasceu: '))
idade = date.today().year - ano
genero = int(
    input(
        '''1 - Masculino \n2 - Feminino \nDigite o número referente ao seu gênero : '''
    ))
if genero == 1:
    if idade < 18:
        print(
            'Você ainda\033[1;31m não\033[m atingiu a idade mínima para a inscrição. Nos vemos daqui a\033[1;31m {} anos!\033[m'
            .format(18 - idade))
    elif idade > 18:
        print(
            'Você ultrapassou em \033[1;31m{} anos\033[m a idade limite para o alistamento.'
            .format(idade - 18))
    else:
        print('Parabéns! Você está\033[32m apto\033[m a se alistar.')
elif genero == 2:
    print('Você não precisa se alistar.')
else:
    print('Opção Inválida')
