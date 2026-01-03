#escreva um programa que faça o pc pensar um número inteiro de 0 a 5
#peça para o usuário tentar advinhar
#o programa deverá dizer se o usuário acertou ou não

import random
número = random.randint(0,5)
nus=int(input('tente advinhar o número que o pc escolheu'))
if número == nus:
    print('você acertou')
else:
    print('você errou, o número selecionado era {}'.format(número))


