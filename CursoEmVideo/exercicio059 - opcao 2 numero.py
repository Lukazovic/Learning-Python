'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1] Somar
[2] Multiplicar
[3] Maior
[4] novos números
[5] Sair do Programa
Seu programa deverá realizar a operação solicitada em cada caso
'''
from time import sleep
print('\n---- Opção entre dois valores ---')

numero1 = float(input('Informe um valor: '))
numero2 = float(input('Informe outro valor: '))

opcao = 0
while opcao != 5:
  print('\nEscolha uma das opções abaixo:')
  print('[1] Somar;')
  print('[2] Multiplicar;')
  print('[3] Maior valor;')
  print('[4] Digitar novos valores;')
  print('[5] Sair do programa.')
  opcao = int(input('Opção: '))

  if opcao == 1:
    print('{} + {} = {}' .format(numero1, numero2, numero1+numero2))
  elif opcao == 2:
    print('{} * {} = {}' .format(numero1, numero2, numero1*numero2))
  elif opcao == 3:
    if numero1 > numero2:
      print('{} é maior do que {}' .format(numero1, numero2))
    elif numero2 > numero1:
      print('{} é maior do que {}' .format(numero2, numero1))
    else:
      print('O números informados são iguais')
  elif opcao == 4:
    numero1 = float(input('\nInforme um valor: '))
    numero2 = float(input('Informe outro valor: '))
  elif opcao == 5:
    print('\nFechando o programa', end='')
    sleep(0.4)
    print('.', end='')
    sleep(0.4)
    print('.', end='')
    sleep(0.4)
    print('.')
    print('')
  else:
    print('ERRO: Opção inválida!')