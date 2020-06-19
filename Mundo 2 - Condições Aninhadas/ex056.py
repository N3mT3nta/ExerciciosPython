mediaid = 0
mulheres20 = 0
maisvelho = ''
maioridade = 0

for c in range(1, 5):
    print(f'\033[1;31mInformações da {c}ª pessoa:\033[m')
    nome = input('Nome: ').strip().title()
    idade = int(input('Idade: '))
    sexo = int(input('Sexo: \n1-Masculino\n2-Feminino\n'))
    mediaid += idade

    if sexo == 2 and idade < 20:
        mulheres20 += 1

    if c == 1 and sexo == 1:
        maioridade = idade
        nomemaisvelho = nome

    if sexo == 1 and maioridade < idade:
        maioridade = idade
        maisvelho = nome

print(f'A média de idade é de {mediaid / 4} anos.')

if maioridade == 0 and maisvelho == '':
    print('Não há homens no grupo.')

else:
    print(f'O homem mais velho tem {maioridade} anos e se chama {maisvelho}.')

if mulheres20 == 0:
    print('Nehuma das mulheres tem menos de 20 anos.')

else:
    print(f'{mulheres20} mulher(es) têm menos de 20 anos.')
