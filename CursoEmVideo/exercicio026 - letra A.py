'''
Faça um programa que leia um frase inteira e mostre:
-> Quantas vezes a letra A aparece;
-> Em que posição a letra A aparece a primeira vez;
-> Em que posição a letra A aparece a última vez;
'''

frase = str(input('Digite uma frase: ')).strip()
frase = str(frase.lower())

print('\nA letra "a" aparece {} vezes na frase digitada' .format(frase.count('a')))

print('A letra "a" aparece a primeira vez na posição {}' .format(frase.find('a') + 1))

print('A letra "a" aparece a última vez vez na posição {}' .format(frase.rfind('a') + 1))