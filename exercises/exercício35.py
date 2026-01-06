#crie um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

#condição de existência de um triângulo:
#Para três segmentos fecharem um triângulo, cada lado deve ser menor que a soma dos outros dois.

a = int(input('lado 1:'))
b = int(input('lado 2:'))
c = int(input('lado 3:'))

if a+b < c and a + c < b and b + c < a:
    print('os segmentos formam um triângulo')
else:
    print('os segmentos não formam um triângulo')

#correção
print('-='*20)
print('analisador de triângulos')
print('-='*20)

r1 = float(input('primeiro segmento:'))
r2 = float(input('segundo segmento:'))
r3 = float(input('terceiro segmento:'))


