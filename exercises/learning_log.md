Curso: Python – Aula 4
Data: 16/12/2025

Conteúdo da aula:comandos básicos
- todos os comandos são funções
- toda função precisa ter parentesis
ex: print("olá,mundo")
-nem tudo no python é mensagem. se você for fazer uma conta, por exemplo:
print(7+4) --> o sistema vai executar e responder 11

mas,se você colocar os números entre aspas, o python vai ler "me mostre esse número"

ex: print ('7'+'4')--> 74

tudo o que estiver entre aspas, é uma mensagem

no python se escreve em letras minúsculas tudo o que não estiver entre aspas

variáveis são espaços na memória onde você pode guardar coisas

toda variável é um objeto no python

um objeto é mais do que uma variável

toda variável é um objeto para o python e pode receber valores 

receber é o mesmo que digitar = 

input é o mesmo que leia

Dúvidas:
- qual é a diferença entre objeto e variável?

Curso: Python – Aula 6
Data: 17/12/2025 a 19/12/25

Conteúdo da aula: tipos primitivos de saída de dados

toda linguagem de programação trabalha basicamente com 4 tipos primitivos / o python tem mais (descbobrir depois)

recomendação sobre simplicidade do código: aspas simples para strings

quando você pede para o python print dois números que são strings ele vai concatenar, ou seja, colocar um ao lado do outro. por isso, você tem que dizer para o python que eles são números usando int

os quatro tipos primitivos mais básicos
- int: numeros inteiros
- float: números 'quebrados'/ex: 4.5
- bool: True ou False / sempre que você usar esse tipo você tem que colocar a letra inicial capitalizada
- str: mensagem / ex: "olá"

Outras formas de usar print

1) print("a soma vale", s)
2) print("a soma vale{}".format(s))

o tipo primitivo tem que ser especificado desde o início

tecla de atalho para executar uma seleção de linhas alt+shift+e

Como converter um número antes de dar print para o formato que você quer
n = float (input('digite um valor:'))
[suponhamos que foi digitado um int, como 4]
print(n)
[quando der print, vai sair 4.0]

#ex6
n = bool (input('digite um valor:'))
print(n) 
se você digita um valor, ele entende [tem um número dentro], então True
se você não digita, então False

dúvidas:
se todo objeto tem atributos e métodos, quais são os tipos de cada um desses que um objeto pode ter?

Curso: Python – Aula 7
Data: 19/12/25
Conteúdo: Operadores aritméticos

- operador + faz adição
- operador - faz subtração
- operador * faz multiplicação
- operador ** faz potência
obs1: outra forma de fazer potência é pow (base, expoente). Cuidado: ao usar essa função interna, a ordem de precedência é perdida
ex: pow (4,3) = 4 elevado a 3 = 64
obs2: dá para fazer raiz na forma de potência. 
ex: raiz quadrada de 9 --> 9**1/2 = 3 
- operador / faz divisão
- operador // faz divisão inteira
- operador % faz resto da divisão

Ordem de precedência

1) ()
2) potências (**)
3) *, /, //, % (se todos aparecerem, resolve quem vier primeiro)
4) +, - 

No caso do python, principalmente para calculos científicos, o limite é o tamanho da memória

Como ajustar o alinhamento do input ao imprimir

Ex: print ('Prazer em te conhecer, {:20}!'.format(nome))
# alinhamento à direita: print ('Prazer em te conhecer, {>:20}!'.format(nome))
# alinhamento à esquerda: print ('Prazer em te conhecer, {<:20}!'.format(nome))
# centralizado: print ('Prazer em te conhecer, {^:20}!'.format(nome))

Observações sobre operações

A criação de uma variável soma é útil se você for armazenar o valor e usar a variável depois.
Em outros casos, você pode simplesmente partir para a operação.
n1 = int (input ('um valor:'))
n2 = int (input ('outro valor:'))
print('a soma vale {}'.format(n1+n2))

Como não quebrar a linha de um print para outro

ex:
normal
print('nome')
print(número)

para não quebrar a linha
print ('nome', end = '  ')
print(número)
obs: você pode colocar praticamente qualquer coisa entre as aspas do end.
ex: poderia ser end =' >>>> '

Como quebrar a linha no meio do print

basta usar \n

ex:
nome = str(input('digite um nome'))
print ('{} é muito legal \n e educada'.format(nome))

f' no começo indica que a string é uma f-string (formatted string). Ela permite colocar variáveis e contas direto dentro do texto, usando { }.
ex: print(f'{nome} tem {idade} anos')

#Aula 08 

Erros para evitar
- variáveis recebem igual, mas a função print não, é errado escrever print = 
- não pode usar o \n no meio de uma lista de operações, porque não é string. Nesse caso, tem que ter uma formatted string e as contas entre colchetes
- Em Python, números decimais usam ponto (.), não vírgula (,).
Quando você escreve 1,15, o Python interpreta isso como uma tupla (1, 15), o que causa erro.