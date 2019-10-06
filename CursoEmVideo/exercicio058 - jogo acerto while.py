from random import randint

print('\n----- JOGO: ACERTANDO NÚMERO DO COMPUTADOR -----')

numeroComp = randint(0,10)

numeroUsuario = -1
contador = 0
while numeroComp != numeroUsuario:
  print('')
  numeroUsuario = int(input('Informe um número: '))
  contador += 1
  if numeroComp != numeroUsuario:
    print('Fail: Tente novamente!')
  else:
    print('\nParabéns!')
    print('Você acertou em {} tentativas' .format(contador))
print('')