import random
import os
import tkinter as tk
from tkinter import messagebox
import time

# Definição da classe Estado
class Estado:
    def __init__(self,  estado_anterior, movimento): 
        """Inicializa o estado com a matriz 3x3.""" 
        if not movimento == None:
             self.matriz =  mover(estado_anterior, movimento) # gera novo estado da matriz
        else:        
            self.matriz = embaralhar(estado_anterior,movimentos=10) # Embaralha a matriz
        
    def avaliar_jogo(self):
        """Avalia se o jogo foi resolvido."""
        matriz_correta = [[1, 2, 3],            # Matriz Gabarito
                          [4, 5, 6],
                          [7, 8, 0]]
        return self.matriz == matriz_correta

def troca(matriz, pos1, pos2):
    """Troca duas posições na matriz e retorna o novo estado da matriz."""
    matriz_copia = matriz
    r1, c1 = pos1
    r2, c2 = pos2
    matriz_copia[r1][c1], matriz_copia[r2][c2] = matriz[r2][c2], matriz[r1][c1]
    return matriz_copia

def mover(matriz, movimento):
    """Move o zero na matriz, se o movimento for válido."""
    linha, coluna = encontrar_posicao_zero(matriz)
    
    if movimento == "W":
        nova_pos = (linha - 1, coluna)
    elif movimento == "S":
        nova_pos = (linha + 1, coluna)
    elif movimento == "A":
        nova_pos = (linha, coluna - 1)
    elif movimento == "D":
        nova_pos = (linha, coluna + 1)
    else:
        return matriz  # Movimento inválido, retorna a matriz sem alterações
    return troca(matriz, (linha, coluna), nova_pos) #Movimento válido, retorna a matriz com a troca

def embaralhar(matriz, movimentos):
    """Embaralha o puzzle fazendo movimentos válidos aleatórios a partir da solução."""
    movimentos_possiveis = ["W", "S", "A", "D"]
    movimentos_opostos = {"W": "S", "S": "W", "A": "D", "D": "A"}
    
    ultimo_movimento = None

    for _ in range(movimentos):
        movimento = random.choice(movimentos_possiveis)
        # Evita que o movimento seja o oposto do anterior
        while (ultimo_movimento and movimento == movimentos_opostos[ultimo_movimento]) or (not validar_movimento(matriz, movimento)):
            movimento = random.choice(movimentos_possiveis)
            ultimo_movimento = movimento

        matriz = mover(matriz, movimento)
    
    return matriz

def encontrar_posicao_zero(matriz):
        """Encontra a posição do zero (espaço vazio) na matriz."""
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] == 0:
                    return i, j
    
def validar_movimento(matriz, movimento):
    """Valida se um movimento é possível."""
    linha, coluna = encontrar_posicao_zero(matriz)
    
    # Verifica o movimento solicitado
    if movimento == "W":
        return linha > 0
    elif movimento == "S":
        return linha < len(matriz) - 1
    elif movimento == "A":
        return coluna > 0
    elif movimento == "D":
        return coluna < len(matriz[0]) - 1
    else:
        return False  # Movimento inválido

# Definição da classe InterfaceGrafica
class InterfaceGrafica:
    def __init__(self, root):
        self.root = root
        self.root.title("8-Puzzle")
        
        self.tamanho_grade = 3
        self.botoes = [[None for _ in range(self.tamanho_grade)] for _ in range(self.tamanho_grade)]
        
        self.criar_botoes()
        self.resetar_jogo()

    def criar_botoes(self):
        """Cria os botões para a interface gráfica."""
        for linha in range(self.tamanho_grade):
            for coluna in range(self.tamanho_grade):
                btn = tk.Button(self.root, font=('Arial', 24), width=4, height=2,
                               command=lambda r=linha, c=coluna: self.click_evento(r, c))
                btn.grid(row=linha, column=coluna)
                self.botoes[linha][coluna] = btn

    def atualizar_botoes(self):
        """Atualiza os botões com base no estado atual do jogo."""
        for linha in range(self.tamanho_grade):
            for coluna in range(self.tamanho_grade):
                valor = self.estado_atual.matriz[linha][coluna]
                if valor == 0:
                    self.botoes[linha][coluna].config(text='', state='disabled')
                else:
                    self.botoes[linha][coluna].config(text=str(valor), state='normal')

    def click_evento(self, linha, coluna):
        """Manipula o clique do botão e faz o movimento correspondente."""
        linha_vazia, coluna_vazia = encontrar_posicao_zero(self.estado_atual.matriz)
        if self.pode_mover(linha, coluna, linha_vazia, coluna_vazia):
            movimento = self.traduzir_movimento(linha, coluna, linha_vazia, coluna_vazia)
            if movimento:
                self.estado_atual = Estado(self.estado_atual.matriz, movimento)
                self.contador_movimentos += 1
                self.atualizar_botoes()
                if self.estado_atual.avaliar_jogo():
                    self.finalizar_jogo()

    def traduzir_movimento(self, linha, coluna, linha_vazia, coluna_vazia):
        """Determina o movimento baseado nas posições das peças."""
        if linha == linha_vazia:
            return "D" if coluna > coluna_vazia else "A"
        elif coluna == coluna_vazia:
            return "S" if linha > linha_vazia else "W"
        return None

    def pode_mover(self, linha, coluna, linha_vazia, coluna_vazia):
        """Verifica se um movimento é possível."""
        return (linha == linha_vazia and abs(coluna - coluna_vazia) == 1) or (coluna == coluna_vazia and abs(linha - linha_vazia) == 1)

    def exibir_mensagem(self, mensagem):
        """Exibe uma mensagem para o usuário."""
        messagebox.showinfo("Informação", mensagem)

    def resetar_jogo(self):
        """Reseta o jogo com um novo estado inicial e reinicia o temporizador."""
        self.estado_atual = Estado([[1, 2, 3], [4, 5, 6], [7, 8, 0]], None)
        self.contador_movimentos = 0
        self.tempo_inicial = time.time()  # Define o tempo inicial
        self.atualizar_botoes()

    def finalizar_jogo(self):
        """Exibe uma mensagem ao finalizar o jogo e pergunta se deseja reiniciar."""
        tempo_decorrido = time.time() - self.tempo_inicial  # Calcula o tempo decorrido
        mensagem = (f"Você venceu!\nMovimentos: {self.contador_movimentos}\n"
                    f"Tempo: {tempo_decorrido:.2f} segundos")
        resposta = messagebox.askyesno("Parabéns!", mensagem + "\nDeseja jogar novamente?")
        
        if resposta:
            self.resetar_jogo()
        else:
            self.root.quit()  # Fecha a aplicação
            
# Função principal
def main():
    """Executa o fluxo principal do jogo com interface gráfica."""
    root = tk.Tk()
    app = InterfaceGrafica(root)
    root.mainloop()

if __name__ == "__main__":
    main()