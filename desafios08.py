#crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
import math
from math import trunc
n = float (input('digite um número'))
print('o número escolhido é {} e sua parte inteira é {}'. format(n, trunc(n)))

#outra resolução
num = float (input ('digite um valor'))
print('o valor escolhido é {} e sua porção inteira é {}'.format(n, int(n)))
#achei difícil, não lembrava a função

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

#faça um programa que leia um ângulo qualquer e mostre na tela o valor so seno, cosseno e tangente desse ângulo
import math
a = int(input('digite o ângulo'))
print('os valores do sen, cos e tg são, respectivamente, {}, {} e {}'.format(math.sin(a), math.cos(a), math.tan(a)))
#errado, não chequei a library reference e não vi que o python calcula em rad, não em º
a = math.radians(float(input('digite um ângulo')))
s=math.sin(a)
c=math.cos(a)
t=math.tan(a)

print('o sen é {}, o cos é {} e a tg é {}'.format(s, c, t))

#um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random
n1 = input('digite o primeiro nome')
n2 = input('digite o segundo nome')
n3 = input('digite o terceiro nome')
n4 = input('digite o quarto nome')
lista = [n1, n2, n3, n4]
sorteado = random.choice(lista)

print(sorteado)
#difícil

#o mesmo professor quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
n1 = input('digite o primeiro nome')
n2 = input('digite o segundo nome')
n3 = input('digite o terceiro nome')
n4 = input('digite o quarto nome')

seq = [n1, n2, n3, n4]
random.shuffle(seq)
print(seq)

