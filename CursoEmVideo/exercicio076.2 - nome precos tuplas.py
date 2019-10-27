'''
Crie um programa que tenha uma tupla única com nome de produtos e seus respectivos
preços, na sequencia.
No final, mostre uma listagem de preços, organizando os dados em forma tabulas.
'''
produtosEprecos = ('Isoporzitos', 3.5, 'Litrão', 8, 'Open Bar', 35, 'Dogão', 6,
'Xerox', 0.15)

print('-'*20)
print('LISTAGEM DE PREÇOS')
print('-'*20)
for i in range(0, len(produtosEprecos), 2):
  print(f'{produtosEprecos[i]} - R$ {produtosEprecos[i+1]:.2f}')
print('-'*20)