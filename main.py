import random
import os

# Definição da classe Estado
class Estado:
    def __init__(self, matriz_inicial):
        """Inicializa o estado com a matriz 3x3."""
        self.matriz = matriz_inicial

    def gerar_sucessor(self, movimento):
        """Gera um novo estado a partir de um movimento válido."""
        # Implementação futura
        pass

    def avaliar_jogo(self):
        """Avalia se o jogo foi resolvido."""
        # Implementação futura
        pass

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
            interface.mostrar_mensagem("Movimento válido.")
            # Aqui você pode adicionar a lógica para aplicar o movimento e atualizar o estado
        else:
            interface.mostrar_mensagem("Movimento inválido, tente novamente.")

# Função principal
def main():
    """Executa o fluxo principal do jogo."""
    estado_inicial = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Exemplo de matriz inicial

    estado = Estado(estado_inicial)  # Instancia a classe Estado
    interface = InterfaceUsuario()  # Instancia a classe InterfaceUsuario

    interface.iniciar_jogo()
    executar_jogo(estado, interface) 

if __name__ == "__main__":
    main()