#aluguel de carros
#escreva um programa que pergunte a qtd de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa 60 reais por dia e 0,15 por km rodados

km=float(input('quantos km foram percorridos?'))
d=int(input('por quantos dias?'))
custo=d*60 + km*0.15
print('o valor a ser pago é {:.2f}'.format(custo))