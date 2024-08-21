import random
import os

# Definição da classe Estado
class Estado:
    def __init__(self,  estado_anterior, movimento): 
        """Inicializa o estado com a matriz 3x3."""
        
        if self.validar_movimento(estado_anterior, movimento):
            self.matriz = self.gerar_sucessor(estado_anterior,movimento)
            
    def embaralhar(self):
        """Embaralha o estado inicial de forma que seja resolvível."""
        # Implementação futura
        pass

    def validar_movimento(self,movimento):
        """Valida se um movimento é possível."""
        # Implementação futura
        return True
        pass

    def gerar_sucessor(self,estado_anterior,movimento):
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
        if movimento == "w":
            novo_estado[row][col] = estado_anterior[row+1][col]
            novo_estado[row+1][col] = 0
        if movimento == "s":
            novo_estado[row][col] = estado_anterior[row-1][col]
            novo_estado[row-1][col] = 0
        if movimento == "a":
            novo_estado[row][col] = estado_anterior[row][col+1]
            novo_estado[row][col+1] = 0
        if movimento == "d":
            novo_estado[row][col] = estado_anterior[row][col-1]
            novo_estado[row][col-1] = 0
            
        return novo_estado
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
        print("Bem-vindo ao jogo dos 8!")
        print("MATRIZ INICIAL:")

    def finalizar_jogo(self):
        """Exibe uma mensagem ao finalizar o jogo."""

# Função principal
def main():
    """Executa o fluxo principal do jogo."""
    estado_inicial = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Exemplo de matriz inicial

    estado = Estado(estado_inicial,"d")  # Instancia a classe Estado

    interface = InterfaceUsuario()  # Instancia a classe InterfaceUsuario
    interface.iniciar_jogo()

    estado.embaralhar()  # Embaralha a matriz inicial (a implementar)
    estado.mostrar()  # Mostra o estado (matriz) atual

    # Aqui você pode adicionar o fluxo principal do jogo (movimentos, etc.)

    interface.finalizar_jogo()  # Finaliza o jogo


if __name__ == "__main__":
    main()
