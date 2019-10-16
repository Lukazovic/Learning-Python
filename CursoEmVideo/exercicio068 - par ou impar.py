# jogo par ou impar que só acaba quando o usuário perder
from random import randint
from time import sleep

nomeJogo = 'PAR OU ÍMPAR'
vitorias = 0
while True:
  print(f'\n{nomeJogo:-^44}')
  numero = int(input('Informe o número que deseja jogar: '))
  while numero < 0:
    numero = int(input('Informe o número que deseja jogar: '))
  opcao = str(input('Escolha entre Par [P] ou Ímpar [I]: ')).strip().upper()
  while opcao not in 'pPiI':
    opcao = str(input('Escolha entre Par [P] ou Ímpar [I]: ')).strip().upper()
  numeroComp = randint(0,10)
  print('\nPAR',end=' ')
  sleep(1)
  print('OU',end=' ')
  sleep(1)
  print('ÍMPAR:')
  sleep(1)
  print(f'Você jogou {numero}')
  print(f'O Computador jogou {numeroComp}')
  resultado = numero + numeroComp
  print(f'O resultado foi {resultado}')
  if resultado % 2 == 0 and opcao == 'P':
    print('\nVocê venceu !')
    print(f'{resultado} é um número Par e você escolheu Par.')
  elif resultado % 2 != 0 and opcao == 'I':
    print('\nVocê venceu !')
    print(f'{resultado} é um número Ímpar e você escolheu Ímpar.')
  elif resultado % 2 == 0 and opcao == 'I':
    print('\nVocê perdeu !')
    print(f'{resultado} é um número Par e você escolheu Ímpar.')
    break
  elif resultado % 2 != 0 and opcao == 'P':
    print('\nVocê perdeu !')
    print(f'{resultado} é um número Ímpar e você escolheu Par.')
    break
  vitorias += 1

print(f'\nVocê venceu {vitorias} vezes\n')