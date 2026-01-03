#escreva um programa que leia a velocidade de um carro
#se ele ultrapasssar 80km/h, escreva uma mensagem de aviso de multa
#a multa vai custar 7 reais por km acima do limite, avise o total para o usuário

v = float(input('qual é a velocidade do carro?'))
if v <= 80:
    print ('você está dentro do limite de velocidade')
else:
    ve = v - 80
    print('você excedeu a velocidade em {} km/h e a multa será de {} reais'.format(ve, ve*7))
