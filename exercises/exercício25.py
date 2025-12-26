#crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input('qual seu nome completo?')).strip()
nome.upper()
nome.find('SILVA')
print(nome == 'SILVA')
#errei

#correção
n = str(input('qual é seu nome completo?')).strip()
print('seu nome tem silva?{}'.format("SILVA" in nome.upper()))

