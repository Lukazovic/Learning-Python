nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2
print('\nSua nota final foi {:.1f}' .format(media))
if media >= 6:
  print('Você ficou a cima da média\n!')
else:
  print('Você ficou abaixo da média!\n')