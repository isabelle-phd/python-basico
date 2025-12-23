#teste
import math
n = int(input('digite um número'))
r = math.sqrt(n)
print('a raiz de {} é igual a {}'.format(n,r))

#outraforma
from math import sqrt, floor
n= int(input('escolha o número'))
r= sqrt(n)
print('a raiz de {} é igual a {:.3f}'.format(n,math.floor(r)))

import random
n = random.random()
n2 = random.randint(1,10)
print (n, n2)

import emoji
print (emoji.emojize("olá, mundo"))

