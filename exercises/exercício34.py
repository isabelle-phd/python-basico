#escreva um programa que pergunte o salário do usuário e calcule o aumento
#para salários maiores que 1250 reais, a=10%
#para inferiores ou iguais, a=15%

s = float(input('digite o salário'))
if s >= 1250:
    print('o salário reajustado será {}'.format(s*1,1))
else:
    print('o salário reajustado será {}'.format(s*1,15))
