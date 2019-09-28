'''
Desenvolva um programa que leia o nome, a idade e o sexo de 4 pessoas. No final 
do programa, mostre:
-A média de idade do grupo;
-Qual o nome do homem mais velho;
-Quantas mulheres têm menos de 20 anos.
'''

countAge = 0
nameOldest = ' '
countAgeWomen = 0
rangePeople = 4

print('\n--- Informações sobre {} pessoas ---' .format(rangePeople))
for i in range(0, rangePeople):
  print('\nInforme os dados nescessários abaixo sobre as pessoas')
  name = str(input('Nome: '))
  age = int(input('Idade: '))
  gender = str(input('Sexo (F ou M): ')).upper()
  
  countAge += age
  if i == 0:
    ageOldest = age
    nameOldest = name
  else:
    if age > ageOldest:
      nameOldest = name
  
  if age < 20 and gender == 'F':
    countAgeWomen += 1

medianAge = countAge / rangePeople


print('\nA média da idade das {} pessoas é de {:.1f} anos' .format(rangePeople, medianAge))
print('{} é o nome da pessoa mais velha' .format(nameOldest))
print('{} é a quantidade de mulheres com menos de 20 anos \n' .format(countAgeWomen))