'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando
o seu preço normal e condição de pagamento:
-À vista dinheiro/cheque: 10% de desconto;
-À vista no cartão: 5% de desconto;
-Em até 2x no cartão: preço normal;
-3x ou mais no cartão: 20% de juros;
'''

print('\n---Preço a ser pago---')
precoProduto = float(input('Informe o preço do produto: '))

print('\nEscolha agora a forma de pagamento:')
print('1 - À vista no dinheiro ou cheque;')
print('2 - À vista no cartão;')
print('3 - Até 2x no cartão;')
print('4 - 3x ou mais no cartão.')
opcao = int(input('Opção desejada: '))

print('')
if opcao == 1:
  print('À vista no dinheiro ou cheque:')
  precoTotal = precoProduto*0.9
  print('O valor a ser pago pelo produto passará de R$ {:.2f} para R$ {:.2f}' .format(
    precoProduto, precoTotal))
elif opcao == 2:
  print('À vista no cartão:')
  precoTotal = precoProduto*0.95
  print('O valor a ser pago pelo produto passará de R$ {:.2f} para R$ {:.2f}' .format(
    precoProduto, precoTotal))
elif opcao == 3:
  print('Até 2x no cartão:')
  precoTotal = precoProduto
  print('O valor não será alterado e continuará R$ {:.2f}')
elif opcao == 4:
  print('Forma de pagamento: À vista no dinheiro ou cheque:')
  precoTotal = precoProduto*1.2
  print('O valor a ser pago pelo produto passará de R$ {:.2f} para R$ {:.2f}' .format(
    precoProduto, precoTotal))
else:
  print('Opção inexistente!')
print('')