'''
Faça um programa que calcule a soma entre todos os números impares que são
multiplos de 3 e que se encontram num intervalor entre 1 até 500
'''

soma = 0
for i in range(1, 501):
  if i%2 != 0 and i%3 == 0:
    soma += i

print('\nA soma dos ímpares múltiplos de três entre 1 e 500 é {}\n' .format(soma))