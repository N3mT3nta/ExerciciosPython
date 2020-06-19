print('\033[1;31mDetector de Palíndromos\033[m')

frase = str(input('Digite a frase sem os acentos: ')).strip().replace(' ', '')
palindromo = frase == frase[::-1]

print(frase)

if palindromo == True:
    print('\033[1;32mA frase é um políndromo')

else:
    print('\033[1;31mA frase não é um políndromo')
