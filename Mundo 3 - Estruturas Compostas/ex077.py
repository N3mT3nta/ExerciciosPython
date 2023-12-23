palavras = 'game', 'vídeo', 'computador', 'placa', 'cabo', 'console', 'programar'
vogais_presentes = ''

for item in palavras:

    '''SEM REPETIÇÃO
    
    for vogal in ['a', 'e', 'i', 'o', 'u']:

            if vogal in item:
                vogais_presentes += f'{vogal} '
    '''
    for caractere in item:
        if caractere in ['a', 'e', 'i', 'o', 'u']:
            vogais_presentes += f'{caractere} '

    print(f'Na palavra {item.upper()} temos {vogais_presentes}')
    vogais_presentes = ''
