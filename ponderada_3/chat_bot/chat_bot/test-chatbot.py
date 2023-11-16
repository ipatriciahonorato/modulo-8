#!/usr/bin/env python3
import re

# Definindo padrões para identificar diferentes comandos do usuário
intent_patterns = {
    r"\b[Vv]á\spara\sa\s(secretaria|biblioteca|cafeteria)": "direcionar_robô",
    r"\b[Dd]irija-se\sao\s(laboratório|auditório)": "direcionar_robô",
    r"\b[Mm]e\sleve\spara\sa\s(biblioteca|sala\sde\saula)": "direcionar_robô"
}

# Ação para mover o robô baseada na localização fornecida
def acao_mover_robô(destino):
    return f"Comando recebido, movendo para {destino}."

# Associando intenções a funções específicas
acoes = {
    "direcionar_robô": acao_mover_robô
}

def main():
    # Executando o loop para receber e processar comandos
    while True:
        comando = input("Informe seu comando (digite 'sair' para finalizar): ")
        if comando.lower() == 'sair':
            break

        encontrado = False
        for expressao, intencao in intent_patterns.items():
            busca = re.compile(expressao)
            resultado = busca.search(comando)
            if resultado:
                print(acoes[intencao](resultado.group(1)))
                encontrado = True
                break

        if not encontrado:
            print("Desculpe, não consegui entender o comando.")

if __name__ == '__main__':
    main()


