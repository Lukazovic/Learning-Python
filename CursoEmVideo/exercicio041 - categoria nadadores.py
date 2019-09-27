'''
A confederação nacional de natação precisa de um programa que leia o ano de
nascimento de um atleta e mostre sua categoria, de acordo com a sua idade:
-Até 9 anos: Mirim;
-Até 14 anos: Infantil;
-Até 19 anos: Junior;
-Até 20 anos: Sênio;
-Acima: Master.
'''
from datetime import date

print('\n---Verificar a categoria dos nadadores---')
anoNascimento = int(input('Informe o ano de nascimento do nadador: '))

idadeNadador = date.today().year - anoNascimento

print('')
if idadeNadador <= 9:
  print('O nadador tem {} anos' .format(idadeNadador))
  print('Categoria: Mirim')
elif idadeNadador > 9 and idadeNadador <= 14:
  print('O nadador tem {} anos' .format(idadeNadador))
  print('Categoria: Infantil')
elif idadeNadador > 14 and idadeNadador <= 19:
  print('O nadador tem {} anos' .format(idadeNadador))
  print('Categoria: Junior')
elif idadeNadador > 19 and idadeNadador <= 20:
  print('O nadador tem {} anos' .format(idadeNadador))
  print('Categoria: Sênior')
else:
  print('O nadador tem {} anos' .format(idadeNadador))
  print('Categoria: Master')
print('')