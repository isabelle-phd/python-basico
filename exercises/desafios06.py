#crie um programa que leia dois números e mostre a soma entre eles
n1= int(input('digite um número:'))
n2= int(input('digite outro número:'))
soma = n1 + n2
print('a soma entre {} e {} vale {}.format(n1, n2, soma))')
#certo

#faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as possíveis informações possíveis sobre ele.
exemplo =input('digite algo:')
print('o tipo primitivo desse valor é', type(exemplo))
print(exemplo.isnumeric())
print(exemplo.isalpha())
print(exemplo.islower())
print(exemplo.isupper())
print(exemplo.istitle())
#correção
exemplo =input('digite algo:')
print('o tipo primitivo desse valor é', type(exemplo))
print('é numérico?', exemplo.isnumeric())
print('contém apenas letras?', exemplo.isalpha())
print('todas as letras são minúsculas?', exemplo.islower())
print('todas as letras são maiúsculas?', exemplo.isupper())
print('a primeira letra é maiúscula?', exemplo.istitle())



