#faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
n=int(input('digite um número'))
print('o número escolhido é {}, seu antecessor é {} e seu sucessor é {}'.format(n, n-1, n+1))

# crie um algoritmo que leia um número e mostre o seu dobro, triplo e a raiz quadrada
#resposta 1
n1=int(input('escolha um número'))
print('o número escolhido é {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {}'.format(n1, n1*2, n1*3, n1**(1/2)))

#resposta 2
n1=int(input('digite um número'))
print('o número escolhido é {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {}'.format(n1, n1*2, n1*3, pow (n1, 1/2)))

# desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
n1=float(input('digite a nota 1'))
n2=float(input('digite a nota 2'))
print('a média do aluno é {}'.format((n1+n2)/2))

# escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
v=float(input('digite o valor'))
print ('o valor em metros é {}, em centímetros é {} e em milímetros é {}'.format(v,v*100, v*1000))

# faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
#reposta 1
n=int(input('escolha um número'))
print(f'{n*1}\n{n*2}\n {n*3}\n {n*4}\n {n*5}\n {n*6}\n {n*7}\n {n*8}\n {n*9}\n {n*10}')

#resposta 2
n=int(input('escolha um número'))
print ('{}x1={}'.format(n,n*1))
print ('{}x1={}'.format(n,n*2))
print ('{}x1={}'.format(n,n*3))

# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere U$$ 1,00 = R$ 3,27
d=float(input('Quantos reais você tem?'))
print('você pode comprar {} dólares'.format(d/3,27))

# faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m^2.
l=float(input('largura?'))
h=float(input('altura?'))
print('se l é {} e h é {}, a área é {} e a qtd de tinta necessária para pintar é {}'.format(l, h, l*h, l*h/2))

