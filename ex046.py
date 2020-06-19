from emoji import emojize
from time import sleep
print('\033[1;31mIniciando contagem regressiva\033[m')
for cr in range(10, -1, -1):
    print(cr)
    sleep(1)
print(emojize(':fireworks: ' * 10, use_aliases=True))
