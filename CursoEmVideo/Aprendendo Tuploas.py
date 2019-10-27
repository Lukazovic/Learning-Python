# TUPLA É IMUTÁVEL

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

for comida in lanche:
  print(f'Quero um {comida}')
print('Obrigado\n')

for pos, comida in enumerate(lanche):
    print(f'Quero um {comida} -> Posição {pos}')
print('ty\n')

# Mostrar a Tupla de maneira ordenada
print(f'Tupula de lanches ordenada: {sorted(lanche)}\n')

# Mais Função de tupla
tuplaA = (1, 2 , 3)
tuplaB = (1, 3, 5)
tuplaC = tuplaA + tuplaB
print(f'Tupla A: {tuplaA}')
print(f'Tupla B: {tuplaB}')
print(f'Tupla C: {tuplaC}')
print(f'Quantas vezes aparece o número 3 na Tupla C: {tuplaC.count(3)}')
print(f'A posição que o número 3 aparace a primeira vez: {tuplaC}')

# É possivel deletar qualquer coisa como uma tupla com o comando del(tuplaC)