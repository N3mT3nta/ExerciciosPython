from time import sleep
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
print('Analisando dados...')
sleep(3)
média = (n1 + n2) / 2
if média < 5:
    print('Com as notas {} e {} a média do aluno é {}. \n\033[1;31m REPROVADO'.
          format(n1, n2, média))
elif média >= 7:
    print('Com as notas {} e {} a média do aluno é {}. \n\033[1;32m APROVADO'.
          format(n1, n2, média))
else:
    print(
        'Com as notas {} e {} a média do aluno é {}. \n\033[1;31m RECUPERAÇÃO'.
        format(n1, n2, média))
