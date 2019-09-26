numero1 = float(input('Informe o primeiro número: '))
numero2 = float(input('Informe o segundo número: '))
numero3 = float(input('Informe o terceiro número: '))

maior = numero1
menor = numero1

if numero2 > maior:
  maior = numero2
else:
  if numero2 < menor:
    menor = numero2

if numero3 > maior:
  maior = numero3
else:
  if numero3 < menor:
    menor = numero3

print('\nO maior número é: {}' .format(maior))
print('O menor número é: {}\n' .format(menor))