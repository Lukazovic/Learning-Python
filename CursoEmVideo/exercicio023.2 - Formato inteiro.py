#Com formato inteiro
numero = int(input('Digite um número de 0 a 9999: '))
'''
#pegando a unidade do número
unidade = numero/10
unidade = unidade - int(unidade)
unidade = int(unidade*10)
print('\nUnidade: {}' .format(unidade))

#Dezena
dezena = int((numero/100 - int(numero/100))*10)
print('Dezena: {}' .format(dezena))

#Centena
centena = int((numero/1000 - int(numero/1000))*10)
print('Centena: {}' .format(centena))

#Milhar
milhar = int((numero/10000 - int(numero/10000))*10)
print('Milhar: {}' .format(milhar))]
'''

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero //1000 % 10
print('\nUindade {}'.format(unidade))
print('Dezena {}'.format(dezena))
print('Centena {}'.format(centena))
print('Milhar {}'.format(milhar))