import tkinter as tk
import random
from tkinter import messagebox

CATEGORIAS = {
    "Objetos": ['caderno', 'video-game', 'computador', 'notebook'],
    "Veículos": ['chevrolet', 'toyota', 'honda', 'ford'],
    "Eletrônicos": ['celular', 'tablet', 'televisão', 'fones de ouvido']
}

NOME_ARQUIVO = "palavras.txt"

class JogoDaAdivinhacao:
    def __init__(self):
        self.palavras = self.ler_palavras()
        if self.palavras:
            self.categoria_escolhida, self.palavra_escolhida = self.selecionar_palavra(self.palavras)
        else:
            self.categoria_escolhida, self.palavra_escolhida = '', ''

        self.num_letras = len(self.palavra_escolhida)
        self.letras_adivinhadas = [' - '] * self.num_letras
        self.letras_digitadas = []
        self.tentativas = 5

        self.root = tk.Tk()
        self.root.title('JOGO DA ADIVINHA!')
        self.largura_minima = 410
        self.altura_minima = 400
        self.largura_maxima = 700
        self.altura_maxima = 600

        self.root.minsize(self.largura_minima, self.altura_minima)
        self.root.maxsize(self.largura_maxima, self.altura_maxima)

        self.categoria_label = tk.Label(self.root, text=f'A palavra pertence à categoria: {self.categoria_escolhida}', padx=10, pady=10, font=('Verdana', 10))
        self.categoria_label.pack()

        self.palavra_label = tk.Label(self.root, text=f'A palavra possui {self.num_letras} letras', padx=10, pady=10, font=('Verdana', 10))
        self.palavra_label.pack()

        self.letras_label = tk.Label(self.root, text=' '.join(self.letras_adivinhadas), padx=10, pady=10, font=('Verdana', 10))
        self.letras_label.pack()

        self.tentativas_label = tk.Label(self.root, text=f'Você tem {self.tentativas} tentativas', padx=10, pady=10, font=('Verdana', 10))
        self.tentativas_label.pack()

        self.letra_entry = tk.Entry(self.root, width=10)
        self.letra_entry.pack()

        self.verificar_button = tk.Button(self.root, text='Verificar', command=self.verificar_letra, bd=5, relief=tk.RAISED, bg='green', fg='black', font=('Verdana', 11), width=10, height=1)
        self.verificar_button.pack()

        self.letras_digitadas_label = tk.Label(self.root, text='Letras digitadas: ', font=('Verdana', 15))
        self.letras_digitadas_label.pack()

        self.mensagem_label = tk.Label(self.root, text='')
        self.mensagem_label.pack()

        self.resultado_label = tk.Label(self.root, text='')
        self.resultado_label.pack()

        self.reiniciar_button = tk.Button(self.root, text='Reiniciar', command=self.reiniciar_jogo, bd=5, relief=tk.RAISED, bg='red', fg='black', font=('Verdana', 8), width=10, height=2)
        self.reiniciar_button.pack(side=tk.LEFT, padx=5, pady=8)

        self.continuar_parar_button = tk.Button(self.root, text='Continuar/Parar', command=self.perguntar_continuar_parar, bd=5, relief=tk.RAISED, bg='black', fg='red', font=('Verdana', 7), width=10, height=2)
        self.continuar_parar_button.pack(side=tk.RIGHT, padx=5, pady=8)

        self.atualizar_tela()

        self.root.mainloop()

    def ler_palavras(self):
        try:
            with open(NOME_ARQUIVO, "r") as arquivo:
                return arquivo.readlines()
        except FileNotFoundError:
            messagebox.showerror("Erro", "Arquivo não encontrado.")
            return []

    def selecionar_palavra(self, palavras):
        linha_aleatoria = random.choice(palavras)
        categoria, palavra = linha_aleatoria.strip().split(":")
        return categoria, palavra

    def reiniciar_jogo(self):
        self.letras_digitadas = []
        self.categoria_escolhida, self.palavra_escolhida = self.selecionar_palavra(self.palavras)
        self.num_letras = len(self.palavra_escolhida)
        self.letras_adivinhadas = [' - '] * self.num_letras
        self.letras_digitadas = []
        self.tentativas = 5

        self.letra_entry.config(state=tk.NORMAL, width=10, justify=tk.CENTER)
        self.verificar_button.config(state=tk.NORMAL)
        self.continuar_parar_button.config(state=tk.NORMAL)
        self.resultado_label.config(text='')
        self.mensagem_label.config(text='')

        self.atualizar_tela()

    def verificar_letra(self):
        letra = self.letra_entry.get().lower()
        self.letras_digitadas.append(letra)
        encontrar_letra = False

        for i in range(self.num_letras):
            if self.palavra_escolhida[i] == letra:
                self.letras_adivinhadas[i] = letra
                encontrar_letra = True

        if encontrar_letra:
            self.mensagem_label.config(text=f'A letra {letra} existe na palavra secreta')
        else:
            self.mensagem_label.config(text=f'A letra {letra} não existe na palavra secreta')
            self.tentativas -= 1

        if ' - ' not in self.letras_adivinhadas:
            self.resultado_label.config(text=f'Parabéns! Você acertou a palavra secreta: {self.palavra_escolhida}'.upper())
            self.letra_entry.config(state=tk.DISABLED)
            self.verificar_button.config(state=tk.DISABLED)
            self.continuar_parar_button.config(state=tk.DISABLED)
        elif self.tentativas == 0:
            self.resultado_label.config(text=f'Você errou, a palavra era: {self.palavra_escolhida}'.upper())
            self.letra_entry.config(state=tk.DISABLED)
            self.verificar_button.config(state=tk.DISABLED)
            self.continuar_parar_button.config(state=tk.DISABLED)

        self.atualizar_tela()
        self.letra_entry.delete(0, tk.END)

    def perguntar_continuar_parar(self):
        resposta = messagebox.askyesno("Continuar ou Parar", "Deseja continuar jogando?")

        if resposta:
            self.reiniciar_jogo()
        else:
            self.root.destroy()

    def atualizar_tela(self):
        self.categoria_label.config(text=f'A palavra pertence à categoria: {self.categoria_escolhida}')
        self.palavra_label.config(text=f'A palavra possui {self.num_letras} letras')
        self.letras_label.config(text=' '.join(self.letras_adivinhadas))
        self.tentativas_label.config(text=f'Você tem {self.tentativas} tentativas')
        self.letras_digitadas_label.config(text=f'Letras digitadas: {self.letras_digitadas}')

if __name__ == "__main__":
    JogoDaAdivinhacao()

