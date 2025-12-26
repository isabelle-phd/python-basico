# faça um programa que leia uma frase e mostre:
# 1) quantas vezes aparece a letra "a"?
# 2) em que posição ela aparece pela primeira vez?
# 3) em que posição ela aparece pela última vez?

frase = str(input('digite uma frase'))
print('A letra a aparece {} vezes nessa frase'.format(frase.count('a'.upper())))
#desse jeito, eu não padronizei, eu pedi para contar todas as minúsculas
#um jeito seria:
#frase = input('Digite uma frase: ')
#frase = frase.lower()
#print('A letra a aparece {} vezes nessa frase'.format(frase.count('a')))

#outro jeito seria
#frase = input('Digite uma frase: ').lower()
#print('A letra a aparece {} vezes nessa frase'.format(frase.count('a')))

print('A letra a aparece {} vezes nessa frase'.format(frase.count('a')))
print('a letra "a" aparece pela primeira vez na posição {}'.format(frase.find('a')))
# não consegui terminar

#correção
frase = str(input('digite uma frase')).upper().strip()
print('A letra a aparece {} vezes nessa frase'.format(frase.count('a')))
print('a letra "a" aparece pela primeira vez na posição {}'.format(frase.find('a')+1))
#nesse caso, colocamos mais um pq a posição 1 para o python é 0
print('a letra "a" aparece pela última vez na posição {}'.format(frase.rfind('a')+1))
