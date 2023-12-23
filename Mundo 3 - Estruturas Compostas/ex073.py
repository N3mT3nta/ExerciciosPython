tabela_brasileirao = ('Bragantino', 'Athletico-PR', 'Fortaleza', 'Palmeiras', 'Atlético-GO',
'Atlético-MG', 'Flamengo', 'Fluminense', 'Bahia', 'Santos',
'Corinthians', 'Ceará SC', 'Internacional', 'Juventude', 'Sport Recife',
'Cuiabá', 'Chapecoense', 'São Paulo', 'América-MG', 'Grêmio')

print(f'''
Tabela do Brasileirão: {tabela_brasileirao}

Os cinco primeiros colocados são {tabela_brasileirao[:5]}

Os quatro últimos colocados são {tabela_brasileirao[-4:]}

Em ordem alfabética: {sorted(tabela_brasileirao)}

A Chapecoense está na posição {tabela_brasileirao.index('Chapecoense') + 1}
''')