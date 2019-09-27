'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar vai perguntar o valor da casa, o salário do comprador
e em quantos anos ele pretende pagar a casa.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado.
'''

valorCasa = float(input('Informe o valor da casa que deseja comprar: '))
salarioComprador = float(input('Informe o seu salário em reais: R$ '))
anosPagamento = int(input('Informe em quantos anos pretende pagar a casa: '))

mesesPagamento = anosPagamento * 12
prestacaoCasa = valorCasa / mesesPagamento

if prestacaoCasa > salarioComprador *0.3 :
  print('\nEmpréstimo negado!\n')
else:
  print('\nO valor da prestação será de R$ {:.2f}\n' .format(prestacaoCasa))