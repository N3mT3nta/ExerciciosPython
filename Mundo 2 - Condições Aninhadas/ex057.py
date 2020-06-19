resposta = ''
vezes = 0

while resposta != 'M' and resposta != 'F':
    if vezes > 0:
        print('\n\033[31mResposta Inválida. Tente novamente.\033[m\n')

    resposta = str(input('Responda:\n\nM - Para masculino\nF - Para feminino\n\n').upper())
    vezes = 1

print('\033[32mObrigado! Tenha um bom dia.')
