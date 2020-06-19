from math import cos, sin, tan, radians
ang = int(input('Informe o ângulo:'))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print(f'Seno: {sen:.2f} \nCosseno: {cos:.2f} \nTangente: {tan:.2f}.')
