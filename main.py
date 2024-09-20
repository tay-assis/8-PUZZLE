import random
import os
import heapq

# Definição da classe Estado
class Estado:
    def __init__(self,  estado_anterior, movimento): 
        """Inicializa o estado com a matriz 3x3.""" 
        if not movimento == None:
             self.matriz = mover(estado_anterior, movimento) # gera novo estado da matriz
        else:        
            self.matriz = embaralhar(estado_anterior, movimentos=100) # Embaralha a matriz
    
    def avaliar_jogo(self):
        """Avalia se o jogo foi resolvido."""
        matriz_correta = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Matriz Gabarito
        if self.matriz == matriz_correta:
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

# Função para trocar posições na matriz
def troca(matriz, pos1, pos2):
    """Troca duas posições na matriz e retorna o novo estado da matriz."""
    matriz_copia = [linha[:] for linha in matriz]  # Copia a matriz
    r1, c1 = pos1
    r2, c2 = pos2
    matriz_copia[r1][c1], matriz_copia[r2][c2] = matriz_copia[r2][c2], matriz_copia[r1][c1]
    return matriz_copia

# Função para mover o zero na matriz
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
    return troca(matriz, (linha, coluna), nova_pos)  # Movimento válido, retorna a matriz com a troca

# Função para embaralhar o puzzle
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

# Função para encontrar a posição do zero na matriz
def encontrar_posicao_zero(matriz):
    """Encontra a posição do zero (espaço vazio) na matriz."""
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 0:
                return i, j

# Função para validar se o movimento é possível
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

class PrioridadeItem:
    def __init__(self, prioridade, g, estado, caminho):
        self.prioridade = prioridade
        self.g = g
        self.estado = estado
        self.caminho = caminho

    # Definir a comparação com base na prioridade (primeiro elemento)
    def __lt__(self, outro):
        return self.prioridade < outro.prioridade

def calcular_heuristica(self, estado):
    """Calcula a heurística de Manhattan (h(n))."""
    h = 0
    posicoes_corretas = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 0: (2, 2)  # Posições corretas do tabuleiro
    }
    
    for i in range(3):
        for j in range(3):
            valor = estado[i][j]
            if valor != 0:
                linha_correta, coluna_correta = posicoes_corretas[valor]
                h += abs(i - linha_correta) + abs(j - coluna_correta)
    
    return h


def busca_a_estrela(estado_inicial, estado_objetivo):
    """Realiza a busca A* com heurística de Manhattan."""
    estrutura = []
    visitados = set()  # Para armazenar estados já visitados
    movimentos_possiveis = ["W", "S", "A", "D"]

    caminho_inicial = []
    estados_visitados = 0

    estado_inicial.mostrar()

    # Adicionar estado inicial na estrutura (fila de prioridade)
    heapq.heappush(estrutura, PrioridadeItem(calcular_heuristica(estado_inicial.matriz, estado_objetivo), 0, estado_inicial, caminho_inicial))
    visitados.add(str(estado_inicial.matriz))

    # Enquanto a estrutura não estiver vazia
    while estrutura:
        item = heapq.heappop(estrutura)  # PrioridadeItem
        g = item.g
        estado_atual = item.estado
        caminho = item.caminho

        # Avaliar estado
        if estado_atual.avaliar_jogo():  # Se for o estado objetivo
            print("Movimentos realizados pela IA até chegar no estado final:")
            print(" -> ".join(caminho))  # Mostrar a sequência de movimentos
            estado_atual.mostrar()  # Mostra o estado final resolvido
            #for movimento in caminho:
                #estado_atual = Estado(estado_atual.matriz, movimento)
                #estado_atual.mostrar()  # Mostrar os estados do caminho final
            print(f"Total de estados visitados: {estados_visitados}")
            return caminho  # Retornar o caminho percorrido

        # Adicionar estados seguintes na estrutura
        for movimento in movimentos_possiveis:
            if validar_movimento(estado_atual.matriz, movimento):
                novo_estado = Estado(estado_atual.matriz, movimento)
                matriz_str = str(novo_estado.matriz)  # Converter para string para verificar se foi visitado
                
                if matriz_str not in visitados:
                    novo_g = g + 1  # Custo do caminho (número de movimentos)
                    novo_h = calcular_heuristica(novo_estado.matriz, estado_objetivo)
                    heapq.heappush(estrutura, PrioridadeItem(novo_g + novo_h, novo_g, novo_estado, caminho + [movimento]))
                    visitados.add(matriz_str)
                    estados_visitados += 1


    # Retornar "Sem solução" se esvaziar a estrutura sem encontrar a solução
    print("Sem solução.")
    print(f"Total de estados visitados: {estados_visitados}")
    return None

def main():
    """Executa o fluxo principal do jogo."""
    estado_objetivo = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Definindo o estado final objetivo

    estados = []
    estados.append(Estado([[1, 2, 3], [4, 5, 6], [7, 8, 0]], None))  # Estado inicial

    interface = InterfaceUsuario()  # Instancia a classe InterfaceUsuario
    interface.iniciar_jogo()

    escolha_ia = input("Deseja que a IA resolva o puzzle? (S/N): ").upper()
    if escolha_ia == "S":
        print("IA começando a resolver o puzzle...")
        busca_a_estrela(estados[-1], estado_objetivo)  # Chama a busca A* com heurística de Manhattan
    else:
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
