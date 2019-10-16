'''
Faça um programa que mostra a tabuada de vários números, um de cada vez, para cada
valor digitado pelo usuário. O programa será interrompido quando o número solicitado
for negativo.
'''
print('\n-----Tabuada-----')

while True:
  
  numero = int(input('\nDigite um número que deseja calcular a tabuada: '))
  if numero < 0:
    break
  print(f'\nTabuada do {numero}:')
  for i in range(1,11):
    print(f'{numero} x {i:2} = {numero*i}')
print('\nFechando o programa...\n')