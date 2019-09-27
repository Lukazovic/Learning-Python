'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo
com a sua idade:
-Se ele ainda vai se alistar ao serviço militar;
-Se é a hora dele se alistar;
-Se já passou do tempo do alistamento.

O programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date

print('\n---Verificar alistamento---')
anoNascimento = int(input('Informe o ano do seu nascimento: '))

idadeAutual = date.today().year - anoNascimento

if idadeAutual < 18:
  print('\nVocê ainda irá se alistar!')
  if 18 - idadeAutual == 1:
    print('Falta 1 ano')
  else:
    print('Faltam: {} anos' .format(18 - idadeAutual))
elif idadeAutual == 18:
  print('\nEstá na hora de você se alistar!')
else:
  print('\nJá passou tempo de você se alistar!')
  if idadeAutual - 18 == 1:
    print('Passou 1 ano')
  else:
    print('Se passaram {} anos' .format(idadeAutual-18))

print('')