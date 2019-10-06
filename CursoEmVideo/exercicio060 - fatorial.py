print('\n----- Fatorial de um número inteiro -----\n')

numero = int(input('Informe um número inteiro: '))

fatorial = 1
contador = numero

print('\n{}! = ' .format(numero), end='')
while contador != 0:
  print('{} ' .format(contador), end='')
  fatorial = fatorial * contador
  contador -= 1
  if contador != 0:
    print('x ', end='')
  else:
    print('= ', end='')

print(fatorial)
print('')