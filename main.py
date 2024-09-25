import copy
import random
import os
import heapq
import copy
from collections import deque
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

    def exibir_menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela
        print("Bem-vindo ao 8-Puzzle!")
        print("Escolha uma opção:")
        print("1. Jogar")
        print("2. Resolver com IA (Busca em Largura)")
        print("3. Resolver com IA (Busca em Profundidade)")
        print("4. Resolver com IA (Busca A*)")
        print("5. Sair")
        
        opcao = input("Digite o número da opção desejada: ")
        return opcao
                
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
    matriz_copia = copy.deepcopy(matriz)
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
    
def jogada_usuario(estados, interface):
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
#--------------IMPLEMENTAÇÃO ESTRELA--------------------------------------------------------------------------            
class NoEstado:
    def __init__(self, matriz, g, h, pai=None):
        self.matriz = matriz
        self.g = g
        self.h = h
        self.f = g + h
        self.pai = pai
        self.filho = None

    def definir_filho(self, filho):
        self.filho = filho

    def __lt__(self, outro):
        return self.f < outro.f
    
    def imprimir_no(self):
        """Função para imprimir todas as informações do nó.""" 
        print("Matriz do estado:")
        for linha in self.matriz:
            print(linha)
        print(f"F: {self.f}, G: {self.g}, H: {self.h}")
        if self.pai:
            print("Este nó tem um pai.")
        else:
            print("Este nó não tem pai.")

    def __str__(self):
        resultado = "\n".join(" | ".join(str(num) if num != 0 else " " for num in linha) for linha in self.matriz)
        resultado += f"\nF: {self.f}, G: {self.g}, H: {self.h}"
        return resultado
    
def busca_a_estrela(matriz_inicial):
    """Implementa a busca A* para resolver o 8-Puzzle.""" 
    global total_estados
    
    estado_inicial = NoEstado(matriz_inicial, 0, 0)
    fila_prioridade = []
    
    heapq.heappush(fila_prioridade, estado_inicial)
    
    visitados = set()
    total_estados = 1  # Inicia com o estado inicial
    
    while fila_prioridade:
        estado_atual = heapq.heappop(fila_prioridade)
        
        # Checa se o estado atual é o objetivo
        if estado_atual.matriz == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
            mostrar_solucao(estado_atual)  # Exibe o caminho da solução
            print(f"Total de estados gerados: {total_estados}")
            print(f"Total de jogadas realizadas: {estado_atual.g}")  # Jogadas realizadas são o custo do caminho
            return
        
        visitados.add(tuple(map(tuple, estado_atual.matriz)))
        
        for proximo_estado in gerar_estados(estado_atual):
            if tuple(map(tuple, proximo_estado.matriz)) not in visitados:
                heapq.heappush(fila_prioridade, proximo_estado)
                total_estados += 1  # Incrementa o contador de estados gerados
    
    print("Sem solução.")
    
def calcular_heuristica(estado):
    """Calcula a heurística (distância de Manhattan).""" 
    matriz_atual = estado.matriz
    heuristica = 0
    
    # Mapeamento das posições corretas para cada número
    pos_correta = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 0: (2, 2)  # Posições corretas do tabuleiro
    }

    for i in range(3):
        for j in range(3):
            num = matriz_atual[i][j]
            if num != 0:
                pos_atual = (i, j)
                # Acessa a posição correta do número 'num'
                pos_correta_num = pos_correta[num]
                # Soma a distância de Manhattan
                heuristica += abs(pos_atual[0] - pos_correta_num[0]) + abs(pos_atual[1] - pos_correta_num[1])
    
    return heuristica

def gerar_estados(estado_atual):
    movimentos_possiveis = ["W", "S", "A", "D"]
    estados = []
    
    for movimento in movimentos_possiveis:
        if validar_movimento(estado_atual.matriz, movimento):
            # Cria uma nova matriz a partir da matriz atual
            nova_matriz = mover(estado_atual.matriz, movimento)  # Aplica o movimento
            
            # Calcula g (custo do caminho) e h (heurística)
            g = estado_atual.g + 1
            h = calcular_heuristica(NoEstado(nova_matriz, g, 0))
            
            # Cria o novo estado como um NoEstado, ligando ao estado atual (pai)
            novo_estado = NoEstado(nova_matriz, g, h, estado_atual)
            
            # Adiciona o novo estado à lista de estados possíveis
            estados.append(novo_estado)
    
    return estados

def imprimir_fila(fila):
    """Imprime os estados na fila de prioridade.""" 
    print("Estados na fila de prioridade:")
    for estado in fila:
        print(estado)
    print("-" * 20)

def mostrar_solucao(estado_final):
    """Exibe o caminho da solução, partindo do estado final até o inicial.""" 
    caminho = []
    estado_atual = estado_final
    
    while estado_atual is not None:
        caminho.append(estado_atual)
        estado_atual = estado_atual.pai
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Resolvendo o Puzzle:\n")
    for estado in reversed(caminho):
        print(estado)
        print("-" * 20)
        
def  busca_largura(estado_inicial):
    Fila = deque()   #definindo estrutura 
    estados_visitados = 0
    caminho_inicial = []
    movimentos_possiveis = ["W", "S", "A", "D"]
    Fila.append((estado_inicial, caminho_inicial))
    
    while Fila:
       
        estado_atual, caminho_atual = Fila.popleft()
        estados_visitados += 1
        
        if estado_atual.avaliar_jogo():  # Se for o estado objetivo
            print("Estado inicial :")
            estado_inicial.mostrar()
            print("Movimentos realizados pela IA até chegar no estado final:")
            print(" -> ".join(caminho_atual))  # Mostrar a sequência de movimentos
            estado_atual.mostrar()  # Mostra o estado final resolvido
            print(f"Total de estados visitados: {estados_visitados}")
            return  # Retornar

        movimentos_validos = []
        for movimento in movimentos_possiveis:
            if validar_movimento(estado_atual.matriz,movimento):
                movimentos_validos.append(movimento)
      
        for movimento in movimentos_validos:
            nova_matriz = copy.deepcopy(estado_atual.matriz)
            novo_estado = Estado(nova_matriz, movimento)
            novo_caminho = caminho_atual + [movimento]  # Atualiza o caminho
            Fila.append((novo_estado, novo_caminho))
    return None  # Se não encontrar solução

# Função principal
def main():
    """Executa o fluxo principal do jogo."""
    
    interface = InterfaceUsuario()  # Instancia a classe InterfaceUsuario

    while True:
        opcao = interface.exibir_menu()

        if opcao == "1":
            estados = []
            estados.append(Estado([[1, 2, 3], [4, 5, 6], [7, 8, 0]], None))  # Estado inicial do jogo
            jogada_usuario(estados, interface)  # Chama a função que faz a jogada do usuário
        elif opcao == "2":
          busca_largura(Estado([[1, 2, 3], [4, 5, 6], [7, 8, 0]], None))
        #elif opcao == "3":
        #    busca_profundidade()
        elif opcao == "4":
            matriz_inicial = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
            matriz_embaralhada = embaralhar(matriz_inicial, movimentos=10)
            busca_a_estrela(matriz_embaralhada)
        elif opcao == "5":
            interface.finalizar_jogo()
            break
        else:
            print("Opção inválida. Tente novamente.")
        
        sair = input("Deseja voltar ao menu principal? (s/n): ")
        if sair.lower() != 's':
            print("Saindo do jogo...")
            break

if __name__ == "__main__":
    main()
