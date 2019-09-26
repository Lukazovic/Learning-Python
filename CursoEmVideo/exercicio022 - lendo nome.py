'''
Desafio 22: Crie um programa que leia o nome completo de uma pessoa e moste:
-O nome com todas as letras maiusculas
-O nome com todas as letras minusculas
-Quantas letras tem o nome todo (sem considerar espaços)
-Quantas letras tem o primeiro nome
'''

nome = str(input('Digite o seu nome: '))

print('\nO seu nome com todas as letras maiusculas fica: ' + nome.upper())

print('O seu nome com todas as letras minusculas fica: ' + nome.lower())

tamanhoNome = len(nome)
contarEspacos = nome.count(' ')
contarLestrasNOme = tamanhoNome-contarEspacos
print('O seu nome tem {} letras' .format(contarLestrasNOme))

listaPalavrasNome = nome.split()
print('O seu primeiro nome é: {}' .format(listaPalavrasNome[0]))