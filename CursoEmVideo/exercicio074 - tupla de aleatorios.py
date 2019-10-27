'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o
maior valor que estão na tupla.
'''
from random import randint

numerosSorteados = (randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))
menorNumero = numerosSorteados[0]
maiorNumero = numerosSorteados[0]
print('\nNúmeros Sorteados')
for i in range(0, len(numerosSorteados)):
  if numerosSorteados[i] < menorNumero:
    menorNumero = numerosSorteados[i]
  if numerosSorteados[i] > maiorNumero:
    maiorNumero = numerosSorteados[i]
  print(numerosSorteados[i])

print(f'\nMenor número: {menorNumero}')
print(f'Maior número: {maiorNumero}\n')