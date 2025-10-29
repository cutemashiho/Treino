import os, math

altura = float (input ('Digite o valor do altura: '))
raio = float (input ('Digite o valor do raio: '))
volume=math.pi*raio*raio*altura
print ('O valor do volume: ' + repr (volume))
print ()
os.system ('pause')