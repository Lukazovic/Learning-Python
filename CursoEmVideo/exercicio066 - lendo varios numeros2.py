'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai
parar quando o usuário digitar o valor 999, que é a condição de parada. No final, 
mostre quantos foram os número digitados e qual foi a soma entre eles (desconsiderando
o 999).
'''
print('\n--- Números digitados ---')
print('Digite 999 para parar o programa\n')

numeroDigitado = -1
soma = 0
contador = 0
while True:
  numeroDigitado = int(input('Informe um número: '))
  if numeroDigitado == 999:
    break
  soma += numeroDigitado
  contador += 1

print(f'\nVocê digitou {contador} números e a soma entre eles foi {soma} \n')