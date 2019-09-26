#Com formato de string
numero = str(input('Digite um número de 0 a 9999: '))

numero = 0000 + numero

print('\nNúmero digitado: {}' .format(numero))
print('Unidade: ' +numero[-1])
print('Dezena: ' +numero[-2])
print('Centena: ' +numero[-3])
print('Milhar: ' +numero[-4])