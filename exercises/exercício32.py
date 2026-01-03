#faça um programa que leia um ano e mostre se ele é bissexto
a = int(input('escolha um ano'))
if a % 4 == 0:
    print('{} é bissexto'.format(a))
else:
    print('{} não é bissexto'.format(a))

