# faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
#reposta 1
n=int(input('escolha um número'))
print(f'{n*1}\n{n*2}\n {n*3}\n {n*4}\n {n*5}\n {n*6}\n {n*7}\n {n*8}\n {n*9}\n {n*10}')

#resposta 2
n=int(input('escolha um número'))
print ('{}x1={}'.format(n,n*1))
print ('{}x2={}'.format(n,n*2))
print ('{}x3={}'.format(n,n*3))

#correção
n=int(input('escolha um número'))
print('_'*12)
print ('{} x {:2f} = {}'.format(n,1,n*1))
print('{} x {:2f} = {}'.format(n, 2, n*2))
print('{} x {:2f} = {}'.format(n, 2, n*2))
print('_'*12)