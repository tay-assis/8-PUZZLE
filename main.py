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
    #estado.mostrar()  # Mostra o estado (matriz) atual

    # Aqui você pode adicionar o fluxo principal do jogo (movimentos, etc.)

    # SIMULÇÃO QUE SERÁ APAGADA COM O DESENVOLVIEMTNO DAS OUTRAS FUNÇÕES DO PRJETO ---------------------------------------------------
    estado_atual = [[1, 2, 3],                          # Simulando um estado embaralhado a ser avaliado
                    [4, 5, 6], 
                    [7, 8, 0]]    
    estado = Estado(estado_atual)                       # Instanciando um novo objeto (novo estado)
    estado.mostrar()                                    # Mostra o estado (matriz) atual
    #-------------------------------------------------------------------------------------------------------------------------------

    estado.avaliar_jogo_1(interface)   

    interface.finalizar_jogo()  # Finaliza o jogo


if __name__ == "__main__":
    main()
