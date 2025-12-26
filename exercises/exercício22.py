#crie um programa que leia o nome completo de uma pessoa e mostre:
#1- o nome com todas as letras maiúsculas
#2 - o nome todas as minúsculas
#3 - quantas letras no total (sem considerar espaços)
#4 - quantas letras tem o primeiro nome

n =(input('digite seu nome completo'))
print(n.upper())
print(n.lower())

n =(input('digite seu nome completo'))
n1= ''.join(n.split())
print(len(n1))

#correção
nome = str(input('digite seu nome completo')).strip()
#a função strip() deixa a string cortada sem espaços antes e depois
print('Analisando seu nome...')
print('seu nome em maiúsculas é...{}'.format(nome.upper()))
print('seu nome em minúsculas é...{}'.format(nome.lower()))
print('seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
print('seu primeiro nome tem {} letras'.format(nome.find(' ')))
#essa última linha tem como objetivo encontrar quando o primeiro espaço aparece

#outra maneira de fazer a última
separa = nome.split()
print('seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))

#minha solução funciona, mas poderia ser melhor

