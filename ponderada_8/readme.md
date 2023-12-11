# Tradutor de Voz e Texto com OpenAI e Chainlit

## Visão Geral
Este projeto apresenta um tradutor de voz e texto que utiliza o modelo de Linguagem de Grande Escala (LLM) da OpenAI. A aplicação capta voz em português, converte-a em texto, traduz para inglês e fornece a resposta em texto e áudio. O projeto se divide em um aplicativo Chainlit para a interface do usuário e um servidor Flask para processamento de áudio.

## Tecnologias Utilizadas
- OpenAI GPT-3.5: Para tradução e geração de áudio.
- Chainlit: Framework para a interface interativa do usuário.
- Python e Ambientes Virtuais (LLM e server_env): Para desenvolvimento e gerenciamento de dependências separadas do aplicativo Chainlit e do servidor Flask.
- React-Speech-Recognition: Biblioteca para captura de voz na interface do usuário.
- Flask: Para criar o servidor de geração de áudio.

## Funcionalidades
- Tradução de Voz para Texto: Conversão de voz em português para texto usando react-speech-recognition.
- Tradução de Texto: Tradução do texto de portExecutando o Aplicativo e o Servidoruguês para inglês.
- Resposta de Áudio: Geração de resposta de áudio em inglês a partir do texto traduzido.

## Configuração de Speech-to-Text

Para capturar a voz do usuário e convertê-la em texto, o projeto utiliza a seguinte configuração no Chainlit:

```
# Permite ao usuário usar voz para texto
[features.speech_to_text]
    enabled = true
    # Veja todas as línguas aqui: https://github.com/JamesBrill/react-speech-recognition/blob/HEAD/docs/API.md#language-string
    language = "pt-BR"
```

## Instalação e Execução

### Clonando o repositório:

```
cd seu_workspace
git clone github.com/ipatriciahonorato/modulo-8.git
cd seu_workspace/modulo-8/ponderada_8
```

### Instalação de Dependências:

Para o aplicativo do chainlit (na pasta raíz do projeto):
```
python3 -m venv llm
source llm/bin/activate
pip install -r requirements.txt
```
Para o servidor(na pasta do server):
```
python3 -m venv server_env
source server_env/bin/activate
pip install -r requirements.txt
```
### Configuração de Variáveis de Ambiente
Crie um arquivo .env na raiz do projeto com a chave de API da OpenAI:

```
OPENAI_API_KEY=sua_chave_de_api_aqui
```
### Executando o aplicativo e servidor

Na pasta raíz, execute:

```
chainlit run app.py -w
```
Na pasta do servidor, execite:
```
flask --app server run --debug
```

### Interagindo com o Tradutor
- Utilize a interface do Chainlit para enviar voz em português.
- Receba a tradução em texto e áudio em inglês.

## Vídeo Demonstrativo

[![Watch the video](http://i3.ytimg.com/vi/vwyDSaoGbnM/hqdefault.jpg)](https://www.youtube.com/watch?v=vwyDSaoGbnM)
