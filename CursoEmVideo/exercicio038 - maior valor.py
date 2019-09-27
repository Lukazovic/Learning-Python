print('\n---Comparação de valores---')
primeiroValor = float(input('Informe o primeiro valor: '))
segundoValor = float(input('Informe o segundo valor: '))

if primeiroValor>segundoValor:
  print('\nO primeiro valor é maior do que o segundo!')
  print('{} > {} \n' .format(primeiroValor, segundoValor))
elif segundoValor>primeiroValor:
  print('\nO segundo valor é maior do que o primeiro!')
  print('{} > {} \n' .format(segundoValor, primeiroValor))
else:
  print('\nO valores são iguais!')
  print('{} = {} \n' .format(primeiroValor, segundoValor))