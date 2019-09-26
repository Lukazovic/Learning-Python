#Faça um programa que pergunte a quantidade de Km percorridas por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
#sabendo que o carro custa R$60 por dias e R$0.15 por Km rodado.

#teste: 8 dias alugados + 720Km = R$588.00

diasAlugado = int(input('\nInforme o número de dias que alugou o carro: '))
kmUsados = float(input('Informe quantos Km rodou com o carro: '))
custoAlguel = diasAlugado*60 + kmUsados*0.15

print('\nO preço a pagar pelo aluguel é: {:.2f}\n' .format(custoAlguel))