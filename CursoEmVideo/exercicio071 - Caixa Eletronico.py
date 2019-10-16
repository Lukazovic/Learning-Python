'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No início,
pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
vai informar quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$ 50, R$20, R$10 e R$1
'''
from time import sleep

print('\n=== CAIXA ELETRÔNICO ===')
valor = int(input('Informe o valor que deseja sacar: '))
while valor < 0:
  print('ERRO: Digite um valor válido!')
  valor = int(input('Informe o valor que deseja sacar: '))
saque = valor
count50 = count20 = count10 = count1 = 0
while saque != 0:
  if saque >= 50:
    count50 += 1
    saque -= 50
  elif saque >= 20:
    count20 += 1
    saque -= 20
  elif saque >= 10:
    count10 += 1
    saque -= 10
  elif saque >= 1:
    count1 += 1
    saque -= 1
print('Calculando as cédulas que o caixa irá entregar',end='')
sleep(0.5)
print('.',end='')
sleep(0.5)
print('.',end='')
sleep(0.5)
print('.',end='')
sleep(0.5)

print('\n\nO Caixa Eletrônico irá retornar:')
print(f'{count50} notas de R$ 50,00')
print(f'{count20} notas de R$ 20,00')
print(f'{count10} notas de R$ 10,00')
print(f'{count1} notas de R$ 1,00\n')