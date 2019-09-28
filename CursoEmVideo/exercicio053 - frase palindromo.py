'''
Crie um programa que leia um frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços
'''

print('\n--- Verificando se uma frase é um Palíndromo ---')
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

#Montando a frase de trás para frente
frase3 = ' '
k = len(frase2)
for i in range(0, len(fraseListada)):
  frase3 = frase3 + ' '
  for j in range(0, len(fraseListada[i])):
    k = k-1
    frase3 = frase3 + frase2[k]
frase3 = frase3.strip()

print('\nPalíndromo: frase ou palavra que se pode ler, indiferentemente, da esquerda para a direita ou vice-versa.')
print('Frase digitada: ' +frase)
print('Frase de trás para frente: ' +frase3)

print('')
if test == 'true':
  print('A frase "{}" é um Palíndromo!' .format(frase))
else:
  print('A frase "{}" não é um Palíndromo!' .format(frase))
print('')