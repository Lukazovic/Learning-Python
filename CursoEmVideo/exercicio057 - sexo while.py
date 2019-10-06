sexo = ' '

while sexo != 'M' and sexo != 'F':

  sexo = str(input('\nDigite seu sexo [M/F]: ')).upper()
  if sexo != 'M' and sexo != 'F':
    print('ERRO: Você não digitou um sexo válido!')
    print('Tente novamente')

if sexo == 'M':
  print('O seu sexo é Masculino')
else:
  print('O seu sexo é Feminino')
print('')