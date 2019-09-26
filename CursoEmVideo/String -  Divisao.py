frase = "Curso em Video Python"

#Dividindo a frase e adicionando a uma lista
palavras_separadas = frase.split()
print(palavras_separadas)

'''
Criando uma frase a partir de uma lista de palavras
neste caso irá gerar uma frase onde cada palravra da lista será juntada com "-"
É possivel juntar apenas com espaços, dai aterar para ' '.join(palavras_separadas)
'''
frase2 = '-'.join(palavras_separadas)
print(frase2)