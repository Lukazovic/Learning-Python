'''
Crie um programa que leia o nome de uma caidade e verifique se começa com 
"Santo" ou não.
'''

cidade = str(input('Digite o nome de uma cidade: ')).strip()
cidade = cidade.lower()

separarNomeCidade = cidade.split()

print('\nA cidade começa com "Santo" ?', 'santo'in separarNomeCidade[0])