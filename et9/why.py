import math
length = 2
x = 1.69458877138639
y = 0.910003603799113
z = 3.79722459403521
a = 41.3796053941184
b = 0.785298339880858
c = 160.62577941976
d = 0.99101928182867
f = math.tanh(math.floor(math.sqrt(length)) - z)
ash = math.asinh(b*length)
g = math.tanh(a*math.floor(ash)%c)
C = math.pow(x,(y*length*f*g - d))
print(C)
