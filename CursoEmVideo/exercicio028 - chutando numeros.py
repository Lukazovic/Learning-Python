from random import randint
from time import sleep

numeroAleatorio = randint(0,5)

print('\nTente acerta o número de 0 a 5')
numeroChutado = int(input('Informe o número escolhido: '))

print('Processando...')
sleep(1)
print(' ')

if numeroAleatorio == numeroChutado:
  print('Parabéns! Você acertou o número {}' .format(numeroAleatorio))
else:
  print('Você escolheu número errado. O número certo era: {}' .format(numeroAleatorio))
print(' ')