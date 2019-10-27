'''
Crie um programa que tenha uma tupla com várias palavras (sem considera acentos).
Depois disso, você deve mostrar, para cada palavra, quais são suas voagais.
'''
tuplasPalavras = ('dicas', 'lucas', 'python', 'programador', 'curso')

print('\nVOGAIS:')
for i in range(0, len(tuplasPalavras)):
  print(f'Na palavra {tuplasPalavras[i].upper()} temos', end=' ')
  for letra in tuplasPalavras[i]:
    if letra in 'aeiou':
      print(letra, end=' ')
  print('')
print('')