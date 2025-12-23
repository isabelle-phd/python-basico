#crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
import math
from math import trunc
n = float (input('digite um número'))
print('o número escolhido é {} e sua parte inteira é {}'. format(n, trunc(n)))

#outra resolução
num = float (input ('digite um valor'))
print('o valor escolhido é {} e sua porção inteira é {}'.format(n, int(n)))
#achei difícil, não lembrava a função