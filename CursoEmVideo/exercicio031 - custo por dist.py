distancia = float(input('Informe a distância da sua viagem em km: '))

if distancia <= 200:
  taxa = 0.5
else:
  taxa = 0.45

custo = distancia * taxa
print('O custo da sua viagem é de R$ {:.2f}' .format(custo))