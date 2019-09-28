from datetime import date

n=7 # Número de pessoas para verificar a maioridade
maiorIdade = 21 # Definindo um número para meior idade
listaIdades = []

print('\n--- Decosbrindo quantas pessoas são maiores de idade entre {} pessoas ---' .format(n))
for i in range(0, n):
  anoNascimento = int(input('Informe a data de nascimento: '))
  if anoNascimento > date.today().year:
    print('ERRO: Data de nascimento inválida!')
  else:
    listaIdades = listaIdades + [date.today().year - anoNascimento]

count = 0
for i in range(0, len(listaIdades)):
  if listaIdades[i] >= maiorIdade:
    count += 1

print('\nDas {} pessoas informadas, {} são maiores de idade*!' .format(n, count))
print('*: Considerando maior idade a partir de {} anos. \n' .format(maiorIdade))