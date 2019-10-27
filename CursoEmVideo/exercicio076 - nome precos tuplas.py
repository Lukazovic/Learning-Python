'''
Crie um programa que tenha uma tupla única com nome de produtos e seus respectivos
preços, na sequencia.
No final, mostre uma listagem de preços, organizando os dados em forma tabulas.
'''
produtosEprecos = ('Isoporzitos', 'Litrão', 'Open Bar', 'Dogão', 'Xerox', 
3.5, 8, 35, 6, 0.15)

print('')
for i in range(0, int(len(produtosEprecos)/2)):
  print(f'{produtosEprecos[i]} - R$ {produtosEprecos[(int(len(produtosEprecos)/2))+i]:.2f}')
print('')