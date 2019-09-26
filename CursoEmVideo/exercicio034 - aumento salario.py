salario = float(input('Informe o valor do salário em reais: R$ '))

if salario > 1250:
  aumento = 10/100
else:
  aumento = 15/100

novoSalario = salario + (salario * aumento)

print('\nO valor do salário aumentará de R$ {:.2f} para R$ {:.2f}' .format(salario, novoSalario))