from math import sqrt, pow, hypot

catetoOposto = float(input('Informe o valor do cateto oposto: '))
catetoAdjacente = float(input('Informe o valor do cateto adjacente: '))
hipotenusa = hypot(catetoAdjacente, catetoOposto)
print('O valor da hipotenusa é: {:.2f}' .format(hipotenusa))