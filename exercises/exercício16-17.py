#um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random
n1 = input('digite o primeiro nome')
n2 = input('digite o segundo nome')
n3 = input('digite o terceiro nome')
n4 = input('digite o quarto nome')
lista = [n1, n2, n3, n4]
sorteado = random.choice(lista)

print(sorteado)
#difícil

#o mesmo professor quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
n1 = input('digite o primeiro nome')
n2 = input('digite o segundo nome')
n3 = input('digite o terceiro nome')
n4 = input('digite o quarto nome')

seq = [n1, n2, n3, n4]
random.shuffle(seq)
print(seq)