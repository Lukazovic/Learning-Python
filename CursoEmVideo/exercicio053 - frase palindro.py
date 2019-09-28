'''
Crie um programa que leia um frase qualquer e diga se ela é um palíndro,
desconsiderando os espaços
'''

print('\n--- Verificando se uma frase é um Palíndro ---')
frase = str(input('Digite uma frase: ')).strip()

fraseListada = frase.lower().split()

frase2 = ' '
for i in range(0, len(fraseListada)):
  frase2 = frase2 + fraseListada[0]
frase2 = frase2.strip()



tamanho = len(frase2)
test = 'true'
for i in range(0, len(frase2)):
  if frase2[i] != frase2[tamanho-1]:
    test = 'false'
  tamanho = tamanho - 1

print('')
if test == 'true':
  print('A frase "{}" é um Palíndro!' .format(frase))
else:
  print('A frase "{}" não é um Palíndro!' .format(frase))
print('')