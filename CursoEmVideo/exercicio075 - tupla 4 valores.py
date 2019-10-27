'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma
tupla. No final, mostre:
(a) Quantas vezes apareceu o valor 9;
(b) Em que posição foi digitado o primeiro valor 3;
(c) Quais foram os números pares.
'''

print('')
numero1 = int(input('Informe um número: '))
numero2 = int(input('Informe um número: '))
numero3 = int(input('Informe um número: '))
numero4 = int(input('Informe um número: '))

tuplaNumeros = (numero1, numero2, numero3, numero4)

print('\n(a) Quantas vezes apareceu o valor 9:')
count = 0
for numero in tuplaNumeros:
  if numero == 9:
    count += 1
print(f'O número 9 foi digitado {count} vezes.')

print('\n(b) Em que posição foi digitado o primeiro valor 3:')
pos3 = -1
for i in range(0,4):
  if tuplaNumeros[i] == 3:
    pos3 = i+1
    break

if pos3 == -1:
  print('Nenhum número 3 foi digitado!')
else:
  print(f'O número 3 foi digitado, primeiramente, na posição {pos3}')

print('\n(c) Números pares:', end=' ')
for numero in tuplaNumeros:
  if numero % 2 == 0:
    print(numero, end=' ')
print('\n')