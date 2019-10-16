from math import pow
from math import sqrt

# ro = float(input('\nRo = '))
# h1 = float(input('h1 = '))
# h2 = float(input('h2 = '))
# h3 = float(input('h3 = '))
# sro = float(input('Sigma Ro1 = '))
# sh1 = float(input('Sigma Sh1 = '))
# sh2 = float(input('Sigma Sh2 = '))
# sh3 = float(input('Sigma Sh3 = '))

ro = 0.997
h1 = 233
h2 = 424
h3 = 482
sro = 0.002
sh1 = 0.5
sh2 = 0.5
sh3 = 0.5


a = (h2-h1)/(h3-h1)
b = ro*(-h3+h2)/pow(h3-h1,2)
c = ro/(h3-h1)
d = ro*(h2-h1)/pow(h3-h1,2)

a = pow(a,2)
b = pow(b,2)
c = pow(c,2)
d = pow(d,2)

a = a*pow(sro,2)
b = b*pow(sh1,2)
c = c*pow(sh2,2)
d = d*pow(sh3,2)

print('\nA = {}' .format(a))
print('B = {}' .format(b))
print('C = {}' .format(c))
print('D = {}' .format(d))

print('\nA + B + C + D = {}' .format(a+b+c+d))
print('RAIZ(A + B + C + D) = {}\n' .format(sqrt(a+b+c+d)))