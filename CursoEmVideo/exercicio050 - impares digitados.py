# Soma dos ímpares digitados pelo usuário

print('\n---Soma dos números ímpares---')

somaImpares = 0
for i in range(0, 6):
  numeroDigitado = int(input('Digite um número inteiro: '))
  if numeroDigitado % 2 != 0:
    somaImpares += numeroDigitado

print('\nA soma dos números ímpares digitador por você deu: {} \n' .format(somaImpares))