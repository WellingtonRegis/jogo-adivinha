
#ADICAO DE BOTOES NA TELA ITERATIVA

import tkinter as tk
import random
from tkinter import messagebox

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

def atualizar_tela():
    categoria_label.config(text=f'A palavra pertence à categoria: {categoria_escolhida}')
    palavra_label.config(text=f'A palavra possui {num_letras} letras')
    letras_label.config(text=' '.join(letras_adivinhadas))
    tentativas_label.config(text=f'Você tem {tentativas} tentativas')
    letras_digitadas_label.config(text=f'Letras digitadas: {letras_digitadas}')

def verificar_letra():
    global tentativas
    letra = letra_entry.get().lower()
    letras_digitadas.append(letra)
    encontrar_letra = False

    for i in range(num_letras):
        if palavra_escolhida[i] == letra:
            letras_adivinhadas[i] = letra
            encontrar_letra = True

    if encontrar_letra:
        mensagem_label.config(text=f'A letra {letra} existe na palavra secreta')
    else:
        mensagem_label.config(text=f'A letra {letra} não existe na palavra secreta')
        tentativas -= 1

    if ' - ' not in letras_adivinhadas:
        resultado_label.config(text=f'Parabéns! Você acertou a palavra secreta: {palavra_escolhida}'.upper())
        letra_entry.config(state=tk.DISABLED, width=30, justify=tk.CENTER)
        verificar_button.config(state=tk.DISABLED)
        continuar_parar_button.config(state=tk.DISABLED)
    elif tentativas == 0:
        resultado_label.config(text=f'Desculpe! Infelizmente você excedeu o número de tentativas e perdeu o jogo. A palavra secreta era: {palavra_escolhida}'.upper())
        letra_entry.config(state=tk.DISABLED, width=10, justify=tk.CENTER)
        verificar_button.config(state=tk.DISABLED)
        continuar_parar_button.config(state=tk.DISABLED)

    atualizar_tela()
    letra_entry.delete(0, tk.END)

def reiniciar_jogo():
    global categoria_escolhida, palavra_escolhida, num_letras, letras_adivinhadas, letras_digitadas, tentativas

    categoria_escolhida = random.choice(list(categorias.keys()))
    palavra_escolhida = random.choice(categorias[categoria_escolhida])
    num_letras = len(palavra_escolhida)
    letras_adivinhadas = [' - '] * num_letras
    letras_digitadas = []
    tentativas = 5

    letra_entry.config(state=tk.NORMAL, width=30, justify=tk.CENTER)
    verificar_button.config(state=tk.NORMAL)
    continuar_parar_button.config(state=tk.NORMAL)
    resultado_label.config(text='')
    mensagem_label.config(text='')

    atualizar_tela()

def perguntar_continuar_parar():
    resposta = messagebox.askyesno("Continuar ou Parar", "Deseja continuar jogando?")

    if resposta:
        reiniciar_jogo()
    else:
        root.destroy()

root = tk.Tk()
root.title('JODO ADIVINHA A PALAVRA !')

# Configuração dos widgets
categoria_label = tk.Label(root, text=f'A palavra pertence à categoria: {categoria_escolhida}')
categoria_label.pack()

palavra_label = tk.Label(root, text=f'A palavra possui {num_letras} letras')
palavra_label.pack()

letras_label = tk.Label(root, text=' '.join(letras_adivinhadas))
letras_label.pack()

tentativas_label = tk.Label(root, text=f'Você tem {tentativas} tentativas')
tentativas_label.pack()

letra_entry = tk.Entry(root, width=10)
letra_entry.pack()

verificar_button = tk.Button(root, text='Verificar', command=verificar_letra)
verificar_button.pack()

letras_digitadas_label = tk.Label(root, text='Letras digitadas: ')
letras_digitadas_label.pack()

mensagem_label = tk.Label(root, text='')
mensagem_label.pack()

resultado_label = tk.Label(root, text='')
resultado_label.pack()

reiniciar_button = tk.Button(root, text='Reiniciar', command=reiniciar_jogo)
reiniciar_button.pack()

continuar_parar_button = tk.Button(root, text='Continuar/Parar', command=perguntar_continuar_parar)
continuar_parar_button.pack()

atualizar_tela()

root.mainloop()
