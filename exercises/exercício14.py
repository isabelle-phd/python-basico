#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
from math import sqrt
ca = float(input('qual é o valor do cateto adjacente?'))
co = float(input('qual é o valor do cateto oposto?'))
h = sqrt(ca**2 + co**2)
print('o valor da hipotenusa é {}'.format(h))

import math
ca = float(input('qual é o valor do cateto adjacente?'))
co = float(input('qual é o valor do cateto oposto?'))
print('o valor da hipotenusa é {}'.format(math.hypot(ca,co)))
#correto