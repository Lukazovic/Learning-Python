'''
Desenvolva um programa que leia o primeiro termo e a razão de uma P.A. No final,
mostre os 10 primeiros termos dessa progressão
'''

print('\n--- Progressão Aritmética ---')
primeiroTermo = int(input('Informe o primeiro termo da P.A.: '))
razaoPA = int(input('Informe a razão da P.A.: '))

print('\nP.A. = ' ,end='')
valorPA = primeiroTermo
for i in range(0,10):
  if i == 0:
    print('[{}, ' .format(valorPA) ,end='')
  elif i > 0 and i < 9:
    valorPA += razaoPA
    print('{}, ' .format(valorPA) ,end='')
  else:
    valorPA += razaoPA
    print('{}] \n'.format(valorPA))