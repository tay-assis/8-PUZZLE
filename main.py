import random
import os

# Definição da classe Estado
class Estado:
    def __init__(self,  estado_anterior, movimento): 
        """Inicializa o estado com a matriz 3x3.""" 
        if not movimento == None:
             self.matriz =  mover(estado_anterior, movimento) # gera novo estado da matriz
        else:        
            self.matriz = embaralhar(estado_anterior,movimentos=100) # Embaralha a matriz
        
    def avaliar_jogo(self):
        """Avalia se o jogo foi resolvido."""

        matriz_correta = [[1, 2, 3],            # Matriz Gabarito
                          [4, 5, 6], 
                          [7, 8, 0]]

        if self.matriz == matriz_correta :
            self.mostrar()
            print("VOCE VENCEU, PARABENS!! - FINALIZANDO JOGO...")
            return True
        else:
            return False

    def mostrar(self):
        """Exibe o estado atual do jogo."""
        for linha in self.matriz:
            print(" | ".join(str(num) if num != 0 else " " for num in linha))
            print("-" * 11)

# Definição da classe InterfaceUsuario
class InterfaceUsuario:
    def iniciar_jogo(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela
        print("Bem-vindo ao jogo dos 8-PUZZLE!")
        print("MATRIZ INICIAL:")
    
    def receber_movimento(self):
        """Recebe um movimento do usuário."""
        movimento = input().upper()
        return movimento

    def mostrar_mensagem(self, mensagem):
        """Exibe uma mensagem para o usuário."""
        print(mensagem)
    
    def finalizar_jogo(self):
        """Exibe uma mensagem ao finalizar o jogo."""
        print("Obrigado por jogar!")

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

def embaralhar(matriz, movimentos=100):
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

# Função principal
def main():
    """Executa o fluxo principal do jogo."""

    estados = []
    estados.append(Estado([[1, 2, 3], [4, 5, 6], [7, 8, 0]], None))  # adiciona Estado inicial do jogo

    interface = InterfaceUsuario()  # Instancia a classe InterfaceUsuario

    interface.iniciar_jogo()
    while not estados[-1].avaliar_jogo(): 
        estado_atual = estados[-1]
        estado_atual.mostrar()  # Mostra o estado (matriz) atual
        interface.mostrar_mensagem("Escolha um movimento (W,S,A,D) ou Q para desistir.")

        movimento = interface.receber_movimento()  # Recebe um movimento do usuário
            
        if movimento == "Q":  # Verifica se o usuário quer desistir
            interface.finalizar_jogo()
            break  # Sai do loop e termina o jogo

        # Verifica se o movimento é válido
        if validar_movimento(estado_atual.matriz, movimento):
            novo_estado = Estado(estado_atual.matriz, movimento)  # Gera um novo estado
            estados.append(novo_estado)
        else:
            interface.mostrar_mensagem("Movimento inválido, tente novamente.")


if __name__ == "__main__":
    main()