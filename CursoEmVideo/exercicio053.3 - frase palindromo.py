'''
Crie um programa que leia um frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços
'''

print('\n--- Verificando se uma frase é um Palíndromo ---')
frase = str(input('Digite uma frase: ')).strip()

palavrasDaFrase = frase.split()
palavrasJuntas = ''.join(palavrasDaFrase)
# ''.join() junta tudo sem espaços
# ' '.join() junta tudo com espaços
# '-'.join() junta tudo separado por -

palavraInversa = ''
palavraInversa = palavrasJuntas[::-1] #percorre a lista de de trás para frente (por isso o -1)

print('\nFrase digitada: ' +palavrasJuntas)
print('\nFrase inversa: ' +palavraInversa)

print('')
if palavrasJuntas == palavraInversa:
  print('Palíndromo!')
else:
  print('Não é um Palíndromo!')
print('')