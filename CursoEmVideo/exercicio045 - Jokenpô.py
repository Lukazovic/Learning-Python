# Crie um programa que faça o computador jogar Jokenpô com você

from random import randint
from time import sleep

opcaoComputador = randint(1,3)

print('\n---Jokenpô---')
print('Selencione uma das opção abaixo: ')
print('1 - Pedra;')
print('2 - Papel;')
print('3 - Tesoura.')
opcaoUsuario = int(input('Opção desejada: '))

sleep(0.5)
print('\nJO' ,end='')
sleep(0.5)
print('KEN' ,end='')
sleep(0.5)
print('PÔ')

print('')
if opcaoUsuario == 1:
  if opcaoComputador == 1:
    print('Empate!')
    print('Você e o computador escolheram "Pedra".')
  elif opcaoComputador == 2:
    print('Você perdeu!')
    print('O computador escolheu "Papel" e você "Pedra".')
  else:
    print('Você venceu!')
    print('O computador escolheu "Tesoura" e você "Pedra".')
elif opcaoUsuario == 2:
  if opcaoComputador == 1:
    print('Você venceu!')
    print('O computador escolheu "Pedra" e você "Papel".')
  elif opcaoComputador == 2:
    print('Empate!')
    print('Você e o computador escolheram "Papel".')
  else:
    print('Você perdeu!')
    print('O computador escolheu "Tesoura" e você "Papel".')
elif opcaoUsuario == 3:
  if opcaoComputador == 1:
    print('Você perdeu!')
    print('O computador escolheu "Pedra" e você "Tesoura".')
  elif opcaoComputador == 2:
    print('Você venceu!')
    print('O computador escolheu "Papel" e você "Tesoura".')
  else:
    print('Empate!')
    print('Você e o computador escolheram "Tesoura".')
else:
  print('Opção Inválida')
print('')
sleep(0.5)