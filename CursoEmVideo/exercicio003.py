number1 = int(input('1st number = '))
number2 = int(input('2nd number = '))
sum = number1 + number2
print('{} + {} = {}' .format(number1, number2, sum))

print('---\nTestando se o valor é um numero---')
n = input('Digite algo: ')
print(n.isnumeric())

print('---Testendo se é letra---')
print(n.isalpha())

print('---Testando se é alfa numerico---')
print(n.isnumeric())

print('---Testando é maiusculo---')
print(n.isupper())

name = input('\nText your name: ')
print('Hello {:-^20}' .format(name), end=' ')
print("testing")