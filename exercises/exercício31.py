#crie um programa que pergunte a distância de uma viagem em km
#calcule o preço da passagem, cobrando 0,5 reais por km até 200km
#e 0,45/km para viagens mais longas

d = float(input('qual é a distância da viagem em km?'))
if d<= 200:
    print('o valor da passagem é {} reais'.format(d*0,5))
else:
    print('o valor da passagem é {}'.format(d*0,45))

