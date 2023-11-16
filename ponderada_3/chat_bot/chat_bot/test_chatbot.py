import rclpy
from rclpy.node import Node
import re

class ChatbotNode(Node):
    def __init__(self):
        super().__init__('chatbot_node')
        self.get_logger().info("Chatbot Node Iniciado")
        
        # Definindo padrões para identificar diferentes comandos do usuário
        self.intent_patterns = {
            r"\b[Vv]á\spara\sa\s(secretaria|biblioteca|cafeteria)": "direcionar_robô",
            r"\b[Dd]irija-se\sao\s(laboratório|auditório)": "direcionar_robô",
            r"\b[Mm]e\sleve\spara\sa\s(biblioteca|sala\sde\saula)": "direcionar_robô"
        }

        # Ação para mover o robô
        self.acoes = {
            "direcionar_robô": self.acao_mover_robô
        }

        # Iniciar o loop de processamento
        self.process_commands()

    def acao_mover_robô(self, destino):
        return f"Comando recebido, movendo para {destino}."

    def process_commands(self):
         # Loop para processar comandos de entrada
        while True:
            comando = input("Informe seu comando (digite 'sair' para finalizar): ")
            if comando.lower() == 'sair':
                break

            encontrado = False
            for expressao, intencao in self.intent_patterns.items():
                busca = re.compile(expressao)
                resultado = busca.search(comando)
                # Se encontrou, executa a ação correspondente e informa
                if resultado:
                    self.get_logger().info(self.acoes[intencao](resultado.group(1)))
                    encontrado = True
                    break

            if not encontrado:
                # Se nenhum comando for reconhecido, informa a situação
                self.get_logger().info("Desculpe, não consegui entender o comando.")

# Funçaão responsável por inicializar o ROS e criar uma instância do nó do ChatBOT
def main(args=None):
    rclpy.init(args=args)
    node = ChatbotNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()



