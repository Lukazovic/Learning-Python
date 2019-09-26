value = float(input('Type a value in metter:'))
km = value/1000
hm = value/100
dm = value/10
decimetros = value*10
cm = value*100
mm = value*1000

print('{}m = {}km'.format(value, km))
print('{}m = {}hm' .format(value, hm))
print('{}m = {}dm' .format(value, dm))
print('{}m = {}dcm' .format(value, decimetros))
print('{}m = {}cm' .format(value, cm))
print('{}m = {}mm' .format(value, mm))