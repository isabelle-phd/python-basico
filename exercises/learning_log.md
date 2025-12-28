# O que é Git
Git é um sistema de controle de versionamento de arquivos, utilizado para:
Guardar o histórico de versões de um software
Registrar quem alterou, quando alterou e o que foi alterado
Manter controle completo de tudo o que você produz
Permitir que várias pessoas alterem o mesmo arquivo simultaneamente
O Git não salva o arquivo inteiro a cada versão. Ele armazena apenas as diferenças (deltas) entre uma versão e outra, mantendo todo o histórico de mudanças.

# O que é GitHub
GitHub é uma plataforma online onde você hospeda projetos que usam Git.
Os projetos ficam organizados em repositórios
Um repositório pode conter vários arquivos
Ao clicar em um arquivo, é possível visualizar o código
Pode ser público (open source) ou privado
Código Open Source
Qualquer pessoa pode ver o código-fonte
Outras pessoas podem usar, estudar ou contribuir com o código

# Repositórios e Fork
Repositório: pasta principal do projeto versionado
Fork: cópia de um repositório de outra pessoa para a sua conta, permitindo modificações independentes

# Branches (Ramificações)
Uma branch é uma ramificação do projeto a partir da linha do tempo principal.
A branch principal é chamada de main ou master
Nela fica o código considerado estável/final
Novas funcionalidades ou alterações são feitas em branches separadas
Exemplo:
O aplicativo do Instagram que você usa corresponde à branch principal (main).
O Git não duplica arquivos entre branches — ele apenas registra as mudanças feitas.

# Commits
Commit é o registro de uma alteração no projeto
Serve para “dizer ao Git” que você alterou algo e criar uma nova versão no histórico

# Merge
Merge é o processo de juntar uma branch com a branch principal
Funciona melhor quando as alterações foram feitas em partes diferentes do código
Fluxo comum:
Voltar para a branch principal
Executar o merge da branch de alterações

# Repositório Remoto
Remote conecta o repositório local (no seu computador) ao GitHub
Permite enviar e receber atualizações
Comandos principais:
Push: envia as alterações do computador para o GitHub
Pull: traz as alterações do GitHub para o computador

# README.md
O arquivo README.md serve para:
Explicar o projeto
Fornecer instruções de uso
Apresentar exercícios, objetivos e estrutura
Funciona como um “leia-me antes de começar”.
Você pode ter:
Um README geral para todo o projeto
Ou um README específico para cada conjunto de exercícios

# Iniciando um Repositório Local
Entrar na pasta do projeto
Abrir o Git Bash
Executar:
git init
A branch principal (main ou master) representa a linha do tempo principal do projeto
git checkout -b nome_da_branch   # cria e muda para uma nova branch
git checkout master              # volta para a branch principal

# Área de Staging
A staging area é onde os arquivos ficam “prontos” para serem commitados
Comandos:
git add nome_do_arquivo
git add .

# Comandos Básicos do Git
git status        # mostra o estado dos arquivos
git commit -m ""  # cria um commit com mensagem
git log           # mostra o histórico de commits
git diff          # mostra as alterações feitas
git restore nome_do_arquivo  # desfaz alterações locais
git checkout master
git merge nome_da_branch

# Aula 4 - 16/12/2025
Conteúdo:comandos básicos

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

# Aula 6 - 17/12/2025 a 19/12/25
Conteúdo: tipos primitivos de saída de dados

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


# Aula 7 - 19/12/25
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
alinhamento à direita: print ('Prazer em te conhecer, {>:20}!'.format(nome))
alinhamento à esquerda: print ('Prazer em te conhecer, {<:20}!'.format(nome))
centralizado: print ('Prazer em te conhecer, {^:20}!'.format(nome))

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

# Aula 08 - 21/12
Conteúdo: Utilizando módulos

- O python trabalha a partir de módulos e pacotes
- O comando import serve para carregar módulos para os programas
- Para o python, listas ficam entre []
- Módulo pygame:
#faça um programa em python que abra e reproduza o áudio de um arquivo mp3
#copie a música da área de trabalho e cole no python
- import pygame
pygame.init()
pygame.mixer.music.load('musica.mp3')

# Aula 09 - 23/12
Conteúdo: Manipulando cadeias de texto

- Fatiar uma string significa pegar "pedaços"
exs: 
print('curso de python')
frase [9]
output: y

frase [1:6]
quando se trabalha com intervalo você sempre tem que colocar +1 no final
por exemplo, curso tem cinco caracteres, então, para conseguir pegar do C até o O, você tem que usar seis caracteres

frase [9:21:2] --> significa que o range é de 9 a 21 e que ele vai pulando de dois em dois
- Python diferencia maiúsculas e minúsculas

frase [:4] --> antes dos dois pontos, é onde a leitura começa, se você omite significa que ele começa do caracter zero.
frase [4:] --> significa que você sabe o começo, mas quer que ele vá até o final/não sabe qual é o último caractere
frase [9::3] --> começa no nove e vai até o fim pulando de três em três

Análise de string
- len(frase) --> qual é o comprimento da frase?
- frase.count('o') --> quantas vezes aparece o "o" minúsculo?
- frase.count('o', 0, 13) --> do caractere zero até o doze quantas x apareceu o "o" minúsculo?
- frase.find('deo') --> em qual posição começa essa letra ou palavra?
- frase.rfind('x')--> procura, mas começa pelo final/direita
- frase.find('string que não existe') --> você pediu para encontrar uma string que não existe e o python vai retornar -1
- 'palavra' in frase --> existe 'palavra' na frase?

Transformação de string
- Via de regra uma string é imutável
- frase.replace('palavra1', 'palavra2') --> onde tiver palavra1 ele vai substituir por palavra2
- frase.upper() --> ele mantém o que é maiúsculo e coloca as demais em maiúsculo
- frase.lower --> oposto do upper
- frase.capitalize () --> deixar só a primeira da frase em maiúscula
- frase.title () --> faz o mesmo que o capitalize, só que com todas as palavras
- frase.strip () --> remove espaços excessivos no início e no final
- frase.rstrip () --> remove só os últimos espaços
- frase.lstrip () --> igual ao anterior, só que começa pela esquerda

Divisão de string
- frase.split() --> ele vai quebrando onde tiver espaço entre as palavras / ele vai gerar uma lista com todas as palavras da lista de caracteres

Junção
- Usar o split e ter todas as palavras em uma lista é útil para fazer junção
- joint(frase) --> junta todos os elementos e pode colocar espaço ou traço onde tinha espaço antes

Funções aprendidas
zfill() é um método de string que preenche a string com zeros à esquerda até atingir o tamanho indicado. É útil para padronizar números digitados com menos dígitos.
Resumo
- zfill() → zeros à esquerda
- rjust() → completa à esquerda com qualquer caractere
- ljust() → completa à direita com qualquer caractere
"45".zfill(4)       → "0045"  # zeros à esquerda
"45".ljust(4, '0')  → "4500"  # zeros à direita

# Revisão

The isidentifier() method returns True if the string is a valid identifier, otherwise False.
A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.

# Dúvidas:
- qual é a diferença entre objeto e variável?
- todo objeto tem atributos e métodos, quais são os tipos de cada um desses que um objeto pode ter?
- o que é um método? o que é uma função?
- qual é a diferença entre métodos e operadores?
- por que para achar as casas decimais se utiliza essa lógica de operadores?
ex da dezena:
“Divida o número por 10 para remover a unidade, depois pegue o resto da divisão por 10 para isolar o último dígito.”
d = num // 10 % 10
3824 (um número de 4 dígitos) dividido por 10 sem resto dá 382
382 // 10 --> depois de formar todas as dezenas possíveis, o que sobra? 2
e por que não pode ser %100? pensando em dinheiro:
% 100 é como dizer:
“Me dê tudo o que sobrou depois de tirar notas de 100” → você recebe R$ 24

// 10 % 10 é como dizer:
“Tire as moedas de R$1 e depois me diga quantas notas de R$10 sobraram que não completam uma de 100” → você recebe 2 notas de R$10
# Erros para evitar
- variáveis recebem igual, mas a função print não, é errado escrever print = 
- não pode usar o \n no meio de uma lista de operações, porque não é string. Nesse caso, tem que ter uma formatted string e as contas entre colchetes
- Em Python, números decimais usam ponto (.), não vírgula (,).
Quando você escreve 1,15, o Python interpreta isso como uma tupla (1, 15), o que causa erro.
