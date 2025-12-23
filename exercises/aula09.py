#ex1
frase = 'constituições são importantes'
print(frase)

#quarta letra
print(frase[3])

#quarta letra até décima terceira
print(frase[3:13])

print(frase[1::2])

#como imprimir textos grandes
print(""""The sun is shining bright and warm, 
It lights up the sky. 
With every star the birds are singing, 
Oh, what a sound! 
It's a beautiful day all around""")

#contar caracteres sem espaço
print(len(frase.strip()))

frase = frase.replace(' ', '*')
print(frase)

print(frase.split())
