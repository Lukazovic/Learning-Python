'''
Desenvolva um programa que leia o comprimento de três retas e dia ao usuário
se elas podem ou não formar um triângulo
'''
import math

linha1 = float(input('Informe o comprimento da primeira linha em metros: '))
linha2 = float(input('Informe o comprimento da segunda linha em metros: '))
linha3 = float(input('Informe o comprimento da terceira linha em metros: '))

test = 1
if (math.fabs(linha1 - linha2) >= linha3) or  (linha3 >= linha1 + linha2):
  test = 0
if (math.fabs(linha2 - linha3) >= linha1) or (linha1 >= linha2 + linha3):
  test = 0
if (math.fabs(linha1 - linha3) >= linha2) or (linha2 >= linha1 + linha3):
  test = 0

if test == 1:
  print('\nAs linhas digitadas podem formar um triângulo')
else:
  print('\nAs linhas digitadas não podem formar um triângulo')