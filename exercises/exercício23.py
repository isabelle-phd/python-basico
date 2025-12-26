#crie um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
n = input('escolha um número de 0 a 9999')
n = n.zfill(4)
print('milhar = {}'.format(n[0]))
print('centena = {}'.format(n[1]))
print('dezena = {}'.format(n[2]))
print('unidade = {}'.format(n[3]))

#correção
num = int(input('informe um número: '))
n = str(num)
print('analisando o número {}'.format(num))
print('unidade = {}'.format(n[3]))
print('dezena = {}'.format(n[2]))
print('centena = {}'.format(n[1]))
print('milhar = {}'.format(n[0]))
#esse código dá erro se o número não tiver quatro dígitos
#outra solução:

num = int(input('informe um número: '))
#retirar string: n = str(num)
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('analisando o número {}'.format(num))
print('unidade = {}'.format(u))
print('dezena = {}'.format(d))
print('centena = {}'.format(c))
print('milhar = {}'.format(m))



