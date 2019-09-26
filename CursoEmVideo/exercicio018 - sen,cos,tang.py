from math import sin, cos, tan, radians

valorAngulo = float(input('Informe o valor do ângulo: '))
senoAngulo = sin(radians(valorAngulo))
cosenoAngulo = cos(radians(valorAngulo))
tangenteAngulo = tan(radians(valorAngulo))

print('\nRadiano:')
print('sen({:.2f}°) = {:.2f}' .format(valorAngulo, senoAngulo))
print('cos({:.2f}°) = {:.2f}' .format(valorAngulo, cosenoAngulo))
print('tang({:.2f}°) = {:.2f}\n' .format(valorAngulo, tangenteAngulo))