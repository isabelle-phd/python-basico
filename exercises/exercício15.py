
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