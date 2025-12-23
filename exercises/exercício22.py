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

