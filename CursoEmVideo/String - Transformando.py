frase = "Curso em Video Python"
print(frase)

#AS TRANSFORMAÇÕES NÃO ALTERAM A FRASE PERMANENTEMENTE

'''
alterando palavras na frase
trocando "Python" por "Android"
'''
print(frase.replace('Python','Android'))

#Mostrando toda a frase em maiusculo
print(frase.upper())

#Mostrando toda a frase em minuscilo
print(frase.lower())

#Deixando apenas a primeira letra em maiusculo
print(frase.capitalize())

#Altera a primeira letra de cada palavra para maiuscolo (a partir dos espaços na frase)
print(frase.title())

#Removendo os espaços excedentes no inicio e no final das frase
frase2 = "   Aprendendo Python   "
print('\n', frase2)
print(frase2.strip())

#Removendo os espaços no final da frase
print(frase2 + '-')
print(frase2.rstrip() + '-')

#Removendo espaços no inicio da frase
print(frase2.lstrip())