import random
import os

# Definição da classe Estado
class Estado:
    def __init__(self,  estado_anterior, movimento): 
        """Inicializa o estado com a matriz 3x3."""  
        self.matriz = self.gerar_sucessor(estado_anterior,movimento)

    def gerar_sucessor(self,estado_anterior, movimento):
        """Gera um novo estado a partir de um movimento válido."""
        novo_estado = estado_anterior
        row = 0
        col = 0
        # Encontrar a posição do zero
        for i in range(3):
            for j in range(3):
                if estado_anterior[i][j] == 0:
                    row = i
                    col = j
        # atualizar a matriz
        if movimento == "W":
            novo_estado[row][col] = estado_anterior[row-1][col]
            novo_estado[row-1][col] = 0
        if movimento == "S":
            novo_estado[row][col] = estado_anterior[row+1][col]
            novo_estado[row+1][col] = 0
        if movimento == "A":
            novo_estado[row][col] = estado_anterior[row][col-1]
            novo_estado[row][col-1] = 0
        if movimento == "D":
            novo_estado[row][col] = estado_anterior[row][col+1]
            novo_estado[row][col+1] = 0
            
        return novo_estado
        pass

    def avaliar_jogo_1(self,interface):
        """Avalia se o jogo foi resolvido."""

        if self.avaliar_jogo_2():
            print("VOCE VENCEU, PARABENS!! - FINALIZANDO JOGO...")
            interface.finalizar_jogo()
        else:
            print("AINDA NAO E A MATRIZ CORRETA")
            print("ENVIAR PARA ALGUMA OUTRA FUNCAO PARA CONTINUAR O JOGO")
        
    def avaliar_jogo_2(self):
        """Avalia se o jogo foi resolvido."""
        
        matriz_correta = [[1, 2, 3],            # Matriz Gabarito
                          [4, 5, 6], 
                          [7, 8, 0]]

        return self.matriz == matriz_correta    # Realizando o retorno Booleano

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

def embaralhar(self):
        """Embaralha o estado inicial de forma que seja resolvível."""
        # Implementação futura
        pass

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
    
# Definição da principal do jogo
def executar_jogo(estado, interface):
    """Executa o loop principal do jogo."""	
    estado.mostrar()  # Mostra o estado (matriz) atual
    interface.mostrar_mensagem("Escolha um movimento (W,S,A,D) ou Q para desistir.")
    while True:  # Loop principal do jogo
        movimento = interface.receber_movimento()  # Recebe um movimento do usuário
            
        if movimento == "Q":  # Verifica se o usuário quer desistir
            interface.finalizar_jogo()
            break  # Sai do loop e termina o jogo

        # Verifica se o movimento é válido
        if validar_movimento(estado.matriz, movimento):
            novo_estado = Estado(estado.matriz, movimento)  # Gera um novo estado
            return novo_estado
        else:
            interface.mostrar_mensagem("Movimento inválido, tente novamente.")

# Função principal
def main():
    """Executa o fluxo principal do jogo."""
    estados= []
    estados_inicial = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Exemplo de matriz inicial
    estados.append(Estado(estados_inicial,"a"))  # Instancia a classe Estado

    interface = InterfaceUsuario()  # Instancia a classe InterfaceUsuario

    interface.iniciar_jogo()

    while not estados[-1].avaliar_jogo():
        estados.append(executar_jogo(estados[-1], interface) )  # Executa o jogo
        for estado in estados:
            estado.mostrar()  # Mostra o estado (matriz) atuala

if __name__ == "__main__":
    main()