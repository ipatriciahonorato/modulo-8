# Chatbot de Segurança Industrial com ChatGPT e LLM

## Visão geral
Este projeto consiste na criação de um chatbot baseado em LLM (Large Language Model) usando a API do ChatGPT para fornecer informações e orientações sobre segurança em ambientes industriais. O objetivo é responder perguntas específicas sobre normas de segurança, procedimentos de emergência e manutenção de equipamentos, de forma clara e informativa.

## Tecnologias Utilizadas

- ChatGPT (OpenAI): Modelo de linguagem avançado para processamento e geração de linguagem natural.
- Langchain: Biblioteca utilizada para integrar o ChatGPT ao chatbot.
- Gradio: Framework para criar interfaces gráficas para o chatbot.
- Python: Linguagem de programação usada para desenvolver o chatbot.
- Anaconda/Miniconda: Ferramenta para gerenciamento de ambientes virtuais e pacotes Python.

## Funcionalidades

- Interpretação de Perguntas de Segurança Industrial: Responde a perguntas relacionadas a normas de segurança, procedimentos de emergência e uso de equipamentos em ambientes industriais.
- Respostas Contextualizadas: Utiliza um prompt de sistema para garantir que as respostas sejam relevantes ao contexto da segurança industrial.
- Streaming de Respostas: Responde em tempo real, com a capacidade de streaming de chunks para melhorar a interação do usuário.

## Instalação e Execução

- Instalação do Miniconda:

```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && bash Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

- Criação de um Ambiente Virtual:

```
conda create -n llm python=3.11
conda activate llm
```

- Instale as Dependências:

```
pip install gradio
pip install langchain
pip install python-dotenv
```

- Clone o Repositório:

```
cd seu_workspace
git clone github.com/ipatriciahonorato/modulo-8.git
 cd seu_workspace/modulo-8/ponderada_4
```


- Execute o Chatbot:

```
python chatbot.py
```

## Vídeo Demonstrativo

Veja o chatbot em ação neste [vídeo](https://drive.google.com/file/d/1cHA8oqbLmZeE8VZDjghDG4yZiFYTJ78n/view) demonstrativo.


