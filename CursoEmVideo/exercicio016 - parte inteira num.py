from math import trunc
numero = float(input('Informe um número real: '))
numeroInt = trunc(numero) #trunc mostra apenas a parte inteira do número
print('A parte inteira de {} é {}' .format(numero, numeroInt))