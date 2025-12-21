#calculando desconto

p=float(input('qual é o preço?'))
d=float(input('qual é o desconto?'))
print('o preço era {}, o desconto era {}%, ficou {}'.format(p, d, p*(1-d/100)))
#certo

#correção
preço = float (input ('qual é o preço do produto?'))
novo = preço - (preço * 5/100)
print('o produto que custava R$ {}, na promoção com desconto de 5% vai custar R$ {}'.format(preço, novo))

#reajuste salarial
#faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s=float(input('qual é seu salário?'))
n= s*1.15
print('seu salário era {:.2f} e, com 15% de aumento, passou a ser {:.2f}'.format(s, n))

#conversor de temperaturas
#escreva um programa que converta uma temperatura de ºC para ºF

t=float(input('qual é a temperatura?'))
f=(t*9/5)+32
print ('{} ºC equivale a {}ºF'.format(t,f))

#aluguel de carros
#escreva um programa que pergunte a qtd de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa 60 reais por dia e 0,15 por km rodados

km=float(input('quantos km foram percorridos?'))
d=int(input('por quantos dias?'))
custo=d*60 + km*0.15
print('o valor a ser pago é {:.2f}'.format(custo))