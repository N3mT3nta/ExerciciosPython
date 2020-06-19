from datetime import date
s = 0
n = 0
for c in range(1,8):
	i = date.today().year - int(input(f'Em que a {c}º pessoa nasceu?: '))
	if i >= 21:
		s = s + 1
	else:
		n = n +1
print(f'{s} destas pessoas atingiram a maioridade.')
print(f'{n} destas pessoas não atingiram a maioridade.')
