print('\n--- P.A. ---\n')

numerosPA = int(input('Informe o primeiro termo da PA: '))
razaoPA = int(input('Informe a razão da PA: '))

contador = 0
print('\nP.A. = [', end=' ')
while contador != 10:
  print(numerosPA, end='')
  numerosPA += razaoPA
  contador += 1
  if contador!=10:
    print(', ', end='')
print('] \n')