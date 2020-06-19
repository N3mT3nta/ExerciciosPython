cid = input('Digite o nome da sua cidade:').strip()
res = 'santo' in cid.lower().split()[0]
print(f'Sua cidade começa com Santo: {res}')
