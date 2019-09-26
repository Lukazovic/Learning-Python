frase = str("Curso em video Python")
print(frase)

print('Printando o tamanho da frase:',len(frase))

print('Contando quantas vezes aparece a letra "o": ', frase.count('o'))

print('Contando quantas vezes aparece a letra "o" do parametro 0 até o 13: ', frase.count('o',0,13))

print('Mostra o parametro que começa as letras "deo" juntas na frase: ', frase.find('deo'))
#se não encontrar as letras juntas na frase retorna -1

print('Existe a palavra "Curso" na frase ? ', 'Curso'in frase)