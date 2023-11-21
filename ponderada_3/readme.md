# Chatbot ROS2 para futura interação com o Robô TurtleBot 3 Burger

## Visão geral

Este projeto apresenta um chatbot simples integrado com ROS2, projetado para interpretar comandos em linguagem natural para interagir com o robô TurtleBot 3 Burger em futuras implementações. O chatbot foi desenvolvido para entender comandos para mover o robô a locais específicos. 

## Tecnologias Utilizadas

 - **ROS2:** Framework robótico utilizado para comunicação e gerenciamento de nós. 
  -  **Python:** Linguagem de programação utilizada para desenvolver o chatbot. 
   - **Expressões Regulares:** Utilizadas para a interpretação de comandos em linguagem natural.

   
## Funcionalidades
 - **Interpretação de Comandos:** O chatbot pode interpretar comandos como "Vá para a secretaria", "Dirija-se ao laboratório", e "Me leve para a biblioteca".
 -  **Dicionário de Intenções e Ações:** Usa um dicionário para mapear comandos a intenções específicas e associá-los a ações correspondentes.
 - **Feedback ao Usuário:** Fornece resposta imediata, confirmando a compreensão e execução dos comandos.
##  Instalação e Execução

1. Clone o Repositório:

   ```
   cd seu_workspace
   git clone github.com/ipatriciahonorato/modulo-8.git
    cd seu_workspace/modulo-8/ponderada_3
   ```

2. **Construa o Pacote com o Colcon:**

    `colcon build --packages-select chat_bot`
   
4. **Fonte o Ambiente ROS2:**

`source install/local_setup.bash`

6. **Execute o script do chatbot via terminal:**

``seu_workspace/src/ponderada_3/chat_bot/chat_bot/./test-chatbot.py``

Após isso o usuário terá acesso ao chatbot para enviar comandos para o robô. 

## Video Demonstrativo

Veja o chatbot em ação neste [vídeo](https://drive.google.com/file/d/1akOmdpdRsKQEEX5yyGtZblJMOVsHq4gi/view) demonstrativo.
