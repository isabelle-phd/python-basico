#crie um script python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada. (Faça todas as soluções possíveis)

#s1
d = int(input('que dia você nasceu?'))
m = int(input('em que mês você nasceu?'))
a = int(input('em que ano você nasceu?'))
#print 1
print('você nasceu em {} de {} de {}'.format(d, m, a))
#print 2
print('você nasceu em', d, 'de', m, 'de', a)

#s2
a= str(input('quando você nasceu? digite no formato dd/mm/aaaa'))
print('você nasceu no dia {}.'.format(a[0:2]))
print('você nasceu no mês {}.'.format(a[3:5]))
print('você nasceu no ano {}.'.format(a[6:10]))

#crie um programa que leia dois números e mostre a soma entre eles
n1=int(input('digite um número: '))
n2=int(input('digite outro número:'))
print('a soma entre {} e {} é {}'.format(n1,n2,n1+n2))

#faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as possíveis informações possíveis sobre ele.
random = input('digite algo')
print(type(random))
print(random.isnumeric())
print(random.isupper())
print(random.isalpha())
print(random.isalnum())

#faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
n = int(input('escolha um número'))
print('0 x {} = {}'.format(n,n*0))
print('1 x {} = {}'.format(n,n*1))
print('2 x {} = {}'.format(n,n*2))

#crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
n = float(input('escolha um número'))
print('o número escolhido é {} e sua porção inteira é {}'.format(n, int(n)))

#faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math
a=math.radians(float(input('digite um ângulo:')))
print(' o ângulo é {}, o sen é {}, o cos é {}, a tg é {}'.format(a, math.sin(a), math.cos(a), math.tan(a)))

#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

#um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

#o mesmo professor quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

#crie um programa que leia o nome completo de uma pessoa e mostre:
#1- o nome com todas as letras maiúsculas
#2 - o nome todas as minúsculas
#3 - quantas letras no total (sem considerar espaços)
#4 - quantas letras tem o primeiro nome
nome=str(input('digite um nome'))
print('seu nome em letras maiúsculas é {}'.format(nome.upper()))
print('seu nome em letras minúsculas é {}'.format(nome.lower()))
print('há {} letras no total'.format(len(nome)-nome.count(' ')))
print('o primeiro nome tem {} letras'.format(nome.find(' ')))

#4 (com explicação escrita para ajudar a não esquecer)
#a primeira etapa é separar todas as partes do nome formando uma lista
lista = nome.split()
#depois, cada elemento vai corresponder a uma posição, ex: [0] será o primeiro nome. Assim:
print('o primeiro nome é {} e tem {} letras'.format(lista[0], len(lista[0])))

#crie um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados


#crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

#crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
n = str(input('digite seu nome completo')).strip().lower()
print('Esse nome tem Silva?'.format(n.find('silva')))

# faça um programa que leia uma frase e mostre:
# 1) quantas vezes aparece a letra "a"?
# 2) em que posição ela aparece pela primeira vez?
# 3) em que posição ela aparece pela última vez?

frase = input('digite uma frase').upper().strip()
print('a letra "a" aparece {} vezes'.format(frase.count('a')))
print('a letra "a" aparece pela primeira vez na posição {}'.format(frase.find(a)+1))
print('a letra "a" aparece pela última vez na posição {}'.format(frase.rfind(a)+1))

