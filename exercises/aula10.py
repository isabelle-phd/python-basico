#ex01
tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')
print('--FIM--')

#como fazer o ex01 de um jeito mais fácil: condição simplificada
tempo = int(input('Quantos anos tem seu carro?'))
print('carro novo' if tempo <= 3 else 'carro velho')
print('--FIM--')

#ex02

nome = str(input('qual é seu nome?'))
if nome == 'Gustavo':
    print('que nome lindo você tem!')
else:
    print('que nome normal')
print('bom dia, {}'.format(nome))

#ex03
n1 = float(input('digite a primeira nota'))
n2 = float(input('digite a segunda nota'))
m = (n1 + n2)/2
print('a média foi {}'.format(m))
if m <= 6.0:
    print('reprovado')
else:
    print('aprovado')
