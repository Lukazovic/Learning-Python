'''
Escreva um programa que leia um número inteiro e peça para o usuário escolhe
qual será a base de conversão:
-1 para binário;
-2 para octal
-3 para hexadecimal
'''

numeroDesejado = int(input('\nInforme um número: '))

print('\nEscolha para qual forma deseja converter este número:')
print('1 - Binário;')
print('2 - Octal;')
print('3 - Hexadecimal.')
opcao = int(input('Opção desejada: '))

if opcao == 1:
  print('\nO número {} em Binário fica: {}\n' .format(numeroDesejado, bin(numeroDesejado)[2:] ))
elif opcao == 2:
  print('\nO número {} em Octal fica: {}\n' .format(numeroDesejado, oct(numeroDesejado)[2:] ))
if opcao == 3:
  print('\nO número {} em Hexadecimal fica: {}\n' .format(numeroDesejado, hex(numeroDesejado)[2:] ))
elif opcao != 1 and opcao != 2 and opcao != 3:
  print('\nERRO: Opção Inexistente!\n')