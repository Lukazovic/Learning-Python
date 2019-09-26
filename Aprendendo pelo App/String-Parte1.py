s = "hello world"
print(s)
print(len(s))

print('\nPrintando apenas alguns paremetros da String: ' + s[0] + s[1])

print('\nPrintando a partir de um certo parametro: ' +s[2:])
print('Ou até um certo parametro: ' +s[:2]) #não inclue o parametro 2

print('\nÉ possível printar o útimo paramtro sem sabe o tamanho da frase: ' +s[-1])

print('\nE pode-se fazer isso: ' + s[:-2] + ' -- ou -- ' +s[-4:])

#Pegar elementos de 1 em 1 da lista
print('\nPegando elementros de 1 e 1 na lista: ' +s[::1])

print('\nPegando elementros de 2 e 2 na lista: ' +s[::2])

print('\nPegando elementros de 1 em 1 e de trás para frente: ' +s[::-1])

print('\nPegando elementos de 1 em 1 apartir do terceiro elemento até o penúltimo: ' +s[3:9:1])