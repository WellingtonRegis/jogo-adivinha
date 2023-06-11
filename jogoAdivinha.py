import random
#JODO DE ADIVINHAR A PALAVRA

categorias = {
    "Objetos": ['caderno', 'video-game', 'computador', 'notebook'],
    "Veículos": ['chevrolet', 'toyota', 'honda', 'ford'],
    "Eletrônicos": ['celular', 'tablet', 'televisão', 'fones de ouvido']
}

categoria_escolhida = random.choice(list(categorias.keys()))
palavra_escolhida = random.choice(categorias[categoria_escolhida])
num_letras = len(palavra_escolhida)
letras_adivinhadas = [' - '] * num_letras
letras_digitadas = []
tentativas = 5

print(f'A palavra pertence à categoria: {categoria_escolhida}')
print(f'A palavra possui {num_letras} letras')
print(' '.join(letras_adivinhadas))

while ' - ' in letras_adivinhadas and tentativas > 0:
    print(f'Você tem {tentativas} tentativas')
    letra = input('Digite uma letra: ')
    print(f'Você digitou a letra {letra}')

    letras_digitadas.append(letra)
    encontrar_letra = False

    for i in range(num_letras):
        if palavra_escolhida[i] == letra:
            letras_adivinhadas[i] = letra
            encontrar_letra = True

    if encontrar_letra:
        print(f'A letra {letra} existe na palavra secreta')
    else:
        print(f'A letra {letra} não existe na palavra secreta')
        tentativas -= 1

    print(''.join(letras_adivinhadas))
    print(f'Letras digitadas: {letras_digitadas}')

if ' - ' not in letras_adivinhadas:
    print(f'Parabéns! Você acertou a palavra secreta: {palavra_escolhida}'.upper())
else:
    print(f'Desculpe! Infelizmente você excedeu o número de tentativas e perdeu o jogo. A palavra secreta era: {palavra_escolhida}'.upper())
