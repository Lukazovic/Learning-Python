print('\n--- Verificando o maior e o menor peso entre 5 pessoas ---')
for i in range(0, 5):
  peso = float(input('Informe o peso de uma pessoa em kg: '))
  if i == 0:
    maiorPeso = peso
    menorPeso = peso
  else:
    if peso > maiorPeso:
      maiorPeso = peso
    elif peso < menorPeso:
      menorPeso = peso

print('\nMaior pesso: {:.1f} kg' .format(maiorPeso))
print('Menor pesso: {:.1f} kg \n' .format(menorPeso))