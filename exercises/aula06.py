#ex1
n1=input('digite um número')
n2=input('digite mais um número')
s= n1+n2
print('a soma vale',s)

#ex2
n1=int(input('digite um número'))
n2=int(input('digite mais um número'))
print('a soma vale',s)

#ex3 - como ver o tipo primitivo
n3 = int(input('digite um valor'))
print(type(n3))

#ex4
na0 = int(input('digite um valor'))
nb0 = int(input('digite mais um valor'))
s0 = na0 + nb0
print('a soma vale',s)

#ex5
na = int(input('digite um valor'))
nb = int(input('digite mais um valor'))
sab = na + nb
print ('a soma entre', na, 'e', nb, 'vale', sab)
#certo, porém sintaxe pouco eficaz

#correção ex5
n4 = int(input('digite um valor'))
n5 = int(input('digite mais um valor'))
s45 = n4 + n5
print ('a soma entre {} e {} vale {}'.format(n4,n5,s45))

#ex6
n = float (input('digite um valor:'))
print(n)

#ex7 - como verificar o tipo primitivo
número = input('digite algo:')
print(número.isnumeric())









