print('\n---Verificar se o aluno foi aprovadou ou não---')
primeiraNota = float(input('Informe a primeira nota: '))
segundaNota = float(input('Informa a segunda nota: '))

media = (primeiraNota + segundaNota)/2

print('')
if media < 5:
  print('Média final: {}' .format(media))
  print('O aluno está repovado!')
elif media >= 5 and media <7:
  print('Média final: {}' .format(media))
  print('O aluno está de recuperação!')
else:
  print('Média final: {}' .format(media))
  print('O aluno está de aprovado!')
print('')