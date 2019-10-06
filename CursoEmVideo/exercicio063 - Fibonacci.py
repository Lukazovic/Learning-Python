print('\n----- Sequência de Fibonacci -----\n')

nTermos = int(input('Informe quantos temros da sequência de Fibonacci deseja mostrar: '))
s1 = 0
s2 = 0
soma = 0
print('Sequência de Fibonacci: ',end='')
for i in range(0, nTermos):
  soma = s1 + s2
  print(soma, end='')
  if i != nTermos-1:
    print(' -> ', end='')
  if i == 0:
    s2 = 1
  s1 = s2
  s2 = soma
print('\n')