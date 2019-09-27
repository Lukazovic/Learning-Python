from math import pow

print('\n---IMC---')
pesoPessoa = float(input('Informe o pesso em kg: '))
alturaPessoa = float(input('Informe a altura em metros: '))

#O IMC é calculado dividindo o peso pela altura elevada ao quadrado.
imc = pesoPessoa / pow(alturaPessoa, 2)

print('')
if imc < 18.5:
  print('Peso: {} kg' .format(pesoPessoa))
  print('Altura: {} m' .format(alturaPessoa))
  print('IMC: {:.2f}' .format(imc))
  print('Abaixo do Peso!')
elif imc >= 18.5 and imc < 25:
  print('Peso: {} kg' .format(pesoPessoa))
  print('Altura: {} m' .format(alturaPessoa))
  print('IMC: {:.2f}' .format(imc))
  print('Peso Ideal!')
elif imc >= 25 and imc < 30:
  print('Peso: {} kg' .format(pesoPessoa))
  print('Altura: {} m' .format(alturaPessoa))
  print('IMC: {:.2f}' .format(imc))
  print('Sobrepeso!')
elif imc >= 30 and imc < 40:
  print('Peso: {} kg' .format(pesoPessoa))
  print('Altura: {} m' .format(alturaPessoa))
  print('IMC: {:.2f}' .format(imc))
  print('Obesidade!')
else:
  print('Peso: {} kg' .format(pesoPessoa))
  print('Altura: {} m' .format(alturaPessoa))
  print('IMC: {:.2f}' .format(imc))
  print('Obesidade mórbida!')
print('')