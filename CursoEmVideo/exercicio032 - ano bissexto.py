from datetime import date

print('\nTestando se um ano é bissexto')
ano = int(input('Informe o ano: '))

print(' ')
if ano == 0:
  ano = date.today().year
if ano % 100 == 0:
  if ano % 400 == 0:
    print('{} é um ano bissexto!' .format(ano))
  else:
    print('{} não é um ano bissexto!' .format(ano))
else:
  if ano % 4 == 0:
    print('{} é um ano bissexto!' .format(ano))
  else:
    print('{} não é um ano bissexto!' .format(ano))
print(' ')