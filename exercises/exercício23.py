#crie um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
n = input('escolha um número de 0 a 9999')
n = n.zfill(4)
print('milhar = {}'.format(n[0]))
print('centena = {}'.format(n[1]))
print('dezena = {}'.format(n[2]))
print('unidade = {}'.format(n[3]))


