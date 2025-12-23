#calculando desconto

p=float(input('qual é o preço?'))
d=float(input('qual é o desconto?'))
print('o preço era {}, o desconto era {}%, ficou {}'.format(p, d, p*(1-d/100)))
#certo

#correção
preço = float (input ('qual é o preço do produto?'))
novo = preço - (preço * 5/100)
print('o produto que custava R$ {}, na promoção com desconto de 5% vai custar R$ {}'.format(preço, novo))

