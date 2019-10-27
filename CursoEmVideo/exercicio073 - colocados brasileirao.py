'''
Crie uma tupla preenchida com os 20 times do Brasileirão, na ordem de colocação.
Depois mostre:
(a) Apenas os 5 primeiros colocados;
(b) Os 4 últimos colocados da tabela;
(c) Uma lista com os times em ordem alfabéfica;
(d) Em que posição está a Chapecoense.
'''

equipes = ('Flamengo', 'Palmeiras', 'Santos', 'São Paulo', 'Internacional',
'Corinthians', 'Grêmio', 'Bahia', 'Athletico-PR', 'Goiás', 'Vasco',
'Atlético-MG', 'Botafogo', 'Fortaleza', 'Ceará', 'Fluminense', 'Cruzeiro',
'CSA', 'Chapecoense', 'Avai')

print('\n(a) os 5 primeiros colocados:')
for i in range (0, 5):
  print(f'{i+1}º {equipes[i]}')

print('\n(b) os 4 últimos colocados:')
for i in range(20-4,20):
  print(f'{i+1}º {equipes[i]}')

print('\n(c) Uma lista dos times em ordem alfabética:')
equipesOrdemAlf = (sorted(equipes))
for i in range(0,20):
  print(f'{equipesOrdemAlf[i]}')

print('\n(d) Colocação da Chapecoense:')
colocacaoChape = 0
while True:
  if equipes[colocacaoChape] == 'Chapecoense':
    break
  colocacaoChape += 1
print(f'{colocacaoChape+1}º {equipes[colocacaoChape]}\n')