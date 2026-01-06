#escreva um programa que faça o pc pensar um número inteiro de 0 a 5
#peça para o usuário tentar advinhar
#o programa deverá dizer se o usuário acertou ou não

import random
from time import sleep

número = random.randint(0,5)
nus=int(input('tente advinhar o número que o pc escolheu'))
if número == nus:
    print('o número escolhido foi {}, você acertou'.format(número))
else:
    print('você errou, o número selecionado era {}'.format(número))

#correção
from random import randint
computador = randint(0,5) #faz o computador pensar
print('vou pensar em um número, tente advinhar...')
jogador = int (input('em que número pensei?'))
print('processando...')
sleep(3)
if jogador == computador:
    print('parabéns, você acertou!')
else:
    print('pensei no número {} e não no {}'.format(computador,jogador))

