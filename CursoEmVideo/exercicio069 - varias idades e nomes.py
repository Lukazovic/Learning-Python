'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
A) Quantas pessoas têm mais de 18 anos;
B) Quantos homens foram cadastrados;
C) Quantas mulheres têm menos de 20 anos.
'''
from time import sleep

contagemCadastros = countMen = countAdult = countWomen = 0
while True:
  print('')
  print('='*50)
  print('NOVO CADASTRO')
  idade = int(input('Informe a idade da pessoa cadastrada: '))
  while idade < 0:
    idade = int(input('Informe a idade da pessoa cadastrada: '))
  sexo = str(input('Informe o sexo da pessa cadastrada [M/F]: ')).strip().upper()
  while sexo not in 'MF':
    sexo = str(input('Informe o sexo da pessa cadastrada [M/F]: ')).strip().upper()
  contagemCadastros += 1
  if idade > 18:
    countAdult += 1
  if sexo == 'M':
    countMen += 1
  if sexo == 'F' and idade < 20:
    countWomen += 1
  print('\nCadastrado com sucesso!')
  opcao = input('Deseja cadastrar uma nova pessoa [S/N]? ').strip().upper()
  while opcao not in 'SN':
    opcao = input('Deseja cadastrar uma nova pessoa [S/N]? ').strip().upper()
  if opcao == 'N':
    break

print('\nContando os dados',end='')
sleep(0.5)
print('.',end='')
sleep(0.5)
print('.',end='')
sleep(0.5)
print('.',end='')

print(f'\n\n{contagemCadastros} pessoas foram cadastradas;')
print(f'{countAdult} ({(100*countAdult/contagemCadastros):.2f}%) pessoas cadastradas têm mais de 18 anos;')
print(f'{countMen} ({(100*countMen/contagemCadastros):.2f}%) homens foram cadastrados;')
print(f'{countWomen} ({(100*countWomen/contagemCadastros):.2f}%) mulheres com menos de 20 anos foram cadastradas.\n')