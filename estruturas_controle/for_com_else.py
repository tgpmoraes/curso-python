# Regras do PEP define que variáveis com letras maiscúla são constantes
PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')
textos = [
    'João gosta de futebol e política',
    'A praia foi divertida',
    'Maria gosta de sair'
]

for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui pelo menos uma palavra proibida', palavra)
            break
    else:
        print('Texto autorizado:', texto)
