moneyInReal = float(input('Digite o valor que você tem na carteira: R$ '))
convertRealToDolar = moneyInReal/4.08
convertRealToEuro = moneyInReal/4.49
print('Com R$ {:.2f} você pode comprar US$ {:.2f} ou ¢ {:.2f}' .format(
  moneyInReal, 
  convertRealToDolar, 
  convertRealToEuro))