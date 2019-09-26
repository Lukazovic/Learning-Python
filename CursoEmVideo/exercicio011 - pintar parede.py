print('Informe as dimensões da parede que deseja pintar.')
alturaParede = float(input('Altura da parede = '))
larguraParede = float(input('Largura da parede = '))
areaParede = alturaParede*larguraParede
print('A sua parede tem dimensão {}mx{}m e área = {}m2' .format(alturaParede,larguraParede, areaParede))

tintaNescessaria = areaParede/2
print('Você precisará de {} litros de tinda para pintar sua parede.' .format(tintaNescessaria))