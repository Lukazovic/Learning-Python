print('\n--- Números primos ---')
numero = int(input('Digite um número: '))

bool = 'true'
for i in range(2, numero):
  if numero % i == 0:
    bool = 'false'

print('')
if bool == 'true':
  print('O número {} é primo!' .format(numero))
else:
  print('O número {} não é primo!' .format(numero))
print('')