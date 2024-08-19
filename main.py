import random
import os

# Definição da classe Estado
class Estado:
    def __init__(self, matriz_inicial):
        """Inicializa o estado com a matriz 3x3."""
        self.matriz = matriz_inicial

    def embaralhar(self):
        """Embaralha o estado inicial de forma que seja resolvível."""
        # Implementação futura
        pass

    def validar_movimento(self, movimento):
        """Valida se um movimento é possível."""
        # Implementação futura
        pass

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
        print("Bem-vindo ao jogo dos 8!")
        print("MATRIZ INICIAL:")

    def finalizar_jogo(self):
        """Exibe uma mensagem ao finalizar o jogo."""

# Função principal
def main():
    """Executa o fluxo principal do jogo."""
    estado_inicial = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Exemplo de matriz inicial

    estado = Estado(estado_inicial)  # Instancia a classe Estado

    interface = InterfaceUsuario()  # Instancia a classe InterfaceUsuario
    interface.iniciar_jogo()

    estado.embaralhar()  # Embaralha a matriz inicial (a implementar)
    estado.mostrar()  # Mostra o estado (matriz) atual

    # Aqui você pode adicionar o fluxo principal do jogo (movimentos, etc.)

    interface.finalizar_jogo()  # Finaliza o jogo


if __name__ == "__main__":
    main()
