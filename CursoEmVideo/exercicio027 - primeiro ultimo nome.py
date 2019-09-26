# Faça um programa que leia um nome inteiro e imprima o primeiro e último nome

nome = str(input('Digite o seu nome completo: '))
nomeDividido = nome.split()

print('\nPrimeiro nome: ' +nomeDividido[0])
print('último nome: ' +nomeDividido[-1])