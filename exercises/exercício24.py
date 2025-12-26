#crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

c = input('qual é o nome da cidade?')
print(c.find('Santo'))
#difícil, não consegui terminar

#correção
cidade = str(input('em qual cidade você nasceu?')).strip()
print(cidade[0:5].upper == 'SANTO')
#esse igual funciona como uma pergunta que vai resultar em true ou false, mas ele não diferencia minúscula e maiúscula ou espaços
#joga tudo para maiúscula/ minúscula na formatação e testa com igual

