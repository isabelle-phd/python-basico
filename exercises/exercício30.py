#crie um programa que leia um número inteiro e mostre na tela se é par ou ímpar

n = int(input('escolha um número'))
if n % 2 == 0:
    print('{} é par'.format(n))
else:
    print('{} é ímpar'.format(n))
