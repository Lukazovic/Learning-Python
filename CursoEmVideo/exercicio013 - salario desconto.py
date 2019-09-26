salarioAtual = float(input('Informe o salário atual de um funcionárioo: R$ '))
novoSalario = salarioAtual+0.15*salarioAtual
print('O funcionário que ganha R$ {:.2f} passará a ganhar R$ {:.2f} após receber 15% de aumento.' 
.format(salarioAtual, novoSalario))