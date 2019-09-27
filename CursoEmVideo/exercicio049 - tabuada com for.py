# tabuada com for

print('\n---Gerando uma Tabuada---')
numero = int(input('Informe um número: '))

print('\nTabuada do {}' .format(numero))
for i in range(1, 11):
  print('{} x {} = {}' .format(numero, i, numero*i))
print('')