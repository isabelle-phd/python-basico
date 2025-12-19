#ex1 - fazendo testes aleatórios com operações
5+3*2
5**2
5**3
19/2
19%2
"oi"+"olá"
oi*5
print ("="*20)

#como dar print com um número x de espaços
nome = input("Digite seu nome: ")
print ('Prazer em te conhecer, {:20}!'.format(nome))

#como deixar um nome centralizado com símbolos em volta
nome = input("Digite seu nome: ")
print ('Prazer em te conhecer, {:=^20}!'.format(nome))

#testando operações
n1 = int (input ('um valor:'))
n2 = int (input ('outro valor:'))
s = n1 + n2
m = n1 * n2
st = n1 - n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print ('a soma é {}, o produto é {} e a divisão é {}'.format(s, m, d))
print ('a divisão inteira é {} e a potência é {}'.format(di, e))

#imprimir sem quebrar a linha
print ('a subtração é {}'.format(st), end='  ')
print('a divisão é {}'.format(d))


#quebrar a linha no meio do print
nome = str(input('Digite um nome: '))
print('{} é muito legal \n e educada'.format(nome))
