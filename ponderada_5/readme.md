# Construção de um Chatbot com LLM da OpenAI

## Visão Geral
Este projeto envolve a criação de um chatbot avançado usando o modelo de Linguagem de Grande Escala (LLM) do ChatGPT 3.5 da OpenAI. O chatbot é projetado para responder perguntas baseadas em conteúdos de documentos PDF, particularmente focado em ["Workshop rules and safety considerations".](https://github.com/ipatriciahonorato/modulo-8/blob/main/ponderada_5/Workshop%20rules%20and%20safety%20considerations%20_%20Students.pdf)

## Tecnologias Utilizadas
- ChatGPT 3.5 (OpenAI): Modelo avançado para processamento e geração de linguagem natural.
- Langchain e PyPDF2: Bibliotecas para processamento de texto e manipulação de PDF.
- Chainlit: Framework para criação da interface do chatbot.
- Python e Ambiente Virtual (venv): Para desenvolvimento e isolamento das dependências do projeto

## Funcionalidades
- Consulta de Normas de Segurança: Capacidade de responder a perguntas baseadas em documentos PDF.
- Interface Gráfica Interativa: Interface amigável para interações fáceis com o usuário.
- Processamento Eficiente de PDF: Extração e utilização do conteúdo textual de PDFs.

## Instalação e Execução

### Clonando o repositório:

```
cd seu_workspace
git clone github.com/ipatriciahonorato/modulo-8.git
cd seu_workspace/modulo-8/ponderada_5
```

### Instalação de Dependências:

```
python3 -m venv llm
source llm/bin/activate
pip install -r requirements.txt
```
### Configuração de Variáveis de Ambiente
Crie um arquivo .env na raiz do projeto com a chave de API da OpenAI:

```
OPENAI_API_KEY=sua_chave_de_api_aqui
```
### Preparação do Arquivo PDF

Utilize o arquivo pdf do documento ["Workshop rules and safety considerations".](https://github.com/ipatriciahonorato/modulo-8/blob/main/ponderada_5/Workshop%20rules%20and%20safety%20considerations%20_%20Students.pdf)

### Executando o ChatBot

```
chainlit run app.py -w
```
### Interagindo com o ChatBot

- Faça o upload do PDF quando solicitado.
- Após o processamento, faça perguntas relacionadas ao conteúdo do PDF.
- Receba respostas baseadas no modelo LLM da OpenAI.

## Vídeo Demonstrativo

Disponível nesse [link]().
