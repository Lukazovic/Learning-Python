numeroExtenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis',
'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

numeroEscolhido = int(input('\nDigite um número entre 0 e 20: '))
while numeroEscolhido<0 and numeroEscolhido>20:
  numeroEscolhido = int(input('ERRO: Digite um número entre 0 e 20: '))

print(f'\nVocê digitou o número {numeroExtenso[numeroEscolhido]}!\n')