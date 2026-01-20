#ex1
print('\033[1;31;43mOlá, Mundo!\033[m')

a = 3
b = 5
print('os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a,b))
#é importante "fechar" as cores para delimitar a parte colorida do texto

#outra forma, com códigos menores
nome = 'Isabelle'
print ('olá, seja bem vinda, {}{}{}'.format('\033[4;34m', nome, '\033[m'))

#extra
nome = 'Isabelle'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo': '\033[33m'}
print ('olá, {}{}{}'.format(cores['amarelo'], nome, cores['azul']))

