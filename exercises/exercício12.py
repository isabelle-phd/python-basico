
# faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m^2.
l=float(input('largura?'))
h=float(input('altura?'))
print('se l é {} e h é {}, a área é {} e a qtd de tinta necessária para pintar é {}'.format(l, h, l*h, l*h/2))
#certo