print('\n--- P.A. ---\n')

primeiroTermo = int(input('Informe o primeiro termo da PA: '))
razaoPA = int(input('Informe a razão da PA: '))

contador = 10
while contador != 0:
  numerosPA = primeiroTermo
  print('\nP.A. = [', end=' ')
  for i in range(0, contador):
    print(numerosPA, end='')
    numerosPA += razaoPA
    if i!= contador-1:
      print(', ', end='')
    else:
      print('] \n')
  contador2 = int(input('Informe quantos termos mais deseja mostrar da PA: '))
  if contador2 != 0:
    contador += contador2
  else:
    contador = 0
print('')

  
