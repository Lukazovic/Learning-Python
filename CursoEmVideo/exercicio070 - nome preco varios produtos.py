'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá
perguntar se o usuário deseja continuar. No final, mostre:
A) Qual é o total gasto na compra;
B) Quantos produtos custam mais de R$ 1000;
C) Qual é o nome do produto mais barato.
'''

count = totalGasto = countMil = 0
nomeProdutoBarato = ''
print('\n===== Lista de produtos comprados =====')
while True:
  nomeProduto = str(input('Informe o nome do produto: ')).strip()
  while not nomeProduto.isalpha():
    nomeProduto = str(input('ERRO: Informe o nome do produto: ')).strip()
  precoProduto = float(input('Informe o preço do produto: '))
  while precoProduto<0:
    precoProduto = float(input('ERRO: Informe o preço do produto: '))
  if count == 0:
    produtoMaisBarato = precoProduto
    nomeProdutoBarato = nomeProduto
  elif precoProduto < produtoMaisBarato:
    nomeProdutoBarato = nomeProduto
  count += 1
  totalGasto += precoProduto
  if precoProduto >= 1000:
    countMil += 1
  opcao = input('Desenha adicionar mais um produto [S/N]? ').strip().upper()
  while opcao not in 'sSnN':
    opcao = input('Desenha adicionar mais um produto [S/N]? ').strip().upper()
  if opcao == 'N':
    break

print(f'\nTotal gasto na compra: R$ {totalGasto:.2f};')
print(f'{countMil} ({(100*countMil/count):.2f}%) produtos custam mais do que R$ 1000;')
print(f'O nome do produto mais barato é "{nomeProdutoBarato}".')