#faça um programa que leia três números e mostre qual é o maior e qual é o menor

n1= float(input('escolha um número'))
n2= float(input('escolha outro número'))
n3= float(input('escolha mais um número'))
#não consegui fazer a lógica com apenas duas condicionais

#tentativa com dica
if n1 <= n2 and n1 <= n3:
    print('o menor valor é {}'.format(n1))
if n2 <= n1 and n2 <= n3:
    print('o menor valor é {}'.format(n2))
if n3 <= n1 and n3 <= n1:
    print('o menor valor é {}'.format(n3))

