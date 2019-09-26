'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre a mensagem dizendo que foi multado.
  A multa vai custar R$7,00 por cada Km acima do limite.
'''

velocidade = float(input('Informe a velocidade, em km/h, do carro: '))

if velocidade > 80.0:
  diferencaVelocidade = velocidade - 80
  valorMulta = diferencaVelocidade * 7
  print('\nVocê excedeu o limite de velocidade em {:.1f} km/h' .format(diferencaVelocidade))
  print('Você foi multado em R$ {:.2f}! \n' .format(valorMulta))
else:
  print('\nA velocidade está dentro do permitido! \n')