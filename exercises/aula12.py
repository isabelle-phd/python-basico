#ex1
n =str(input('qual é seu nome?'))
if n == 'julia':
    print('que lindo')
elif n == 'lucas' or n == 'joaquim':
    print('uau')
elif n in 'marina luciana carlota':
#essa linha significa uma lista com os nomes que podem corresponder ao comando seguinte
    print('lindo nome feminino')
else:
    print('seu nome é normal')
print('tenha um bom dia {}'.format(n))

