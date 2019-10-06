'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e menor valor lido. O
programa deve perguntar ao usuário se ele quer continuar ou não a digitar valores.
'''

verificacao = ' '
contador = 0
maiorValor = 0
menorValor = 0
soma = 0
while verificacao not in 'Nn':
  numero = int(input('\nDigite um número: '))
  if contador == 0:
    maiorValor = numero
    menorValor = numero
  elif numero > maiorValor:
    maiorValor = numero
  elif menorValor < numero:
    menorValor = numero
  soma += numero
  contador += 1
  verificacao = str(input('Deseja digitar outro valor ? [S/N]: ')).strip()
  while verificacao not in 'SsNn':
    print('Erro: Opção inexistente!')
    verificacao = str(input('Deseja digitar outro valor ? [S/N]: ')).strip()

media = soma/contador

print('\nA média de todos os valores é {}' .format(media))
print('O maior valor é {}' .format(maiorValor))
print('O menor valor é {}\n' .format(menorValor))