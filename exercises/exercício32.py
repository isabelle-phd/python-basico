#faça um programa que leia um ano e mostre se ele é bissexto
a = int(input('escolha um ano'))
if a % 4 == 0:
    print('{} é bissexto'.format(a))
else:
    print('{} não é bissexto'.format(a))

#correção
#faltaram algumas condicionais
#anos bissextos acontecem a cada 4 anos, exceto anos múltiplos de 100
#que não são múltiplos de 400


from datetime import date
a = int(input('escolha um ano. coloque 0 para analisar o ano atual'))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('{} é bissexto'.format(a))
else:
    print('{} não é bissexto'.format(a))

# % 100 != 0 significa que o resto da divisão por cem não é zero
# or significa duas regras independentes juntas