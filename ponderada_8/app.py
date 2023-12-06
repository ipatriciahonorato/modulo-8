# Importação das bibliotecas

import os
import openai
import pickle
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
from langchain.chat_models import ChatOpenAI
import chainlit as cl
import time
import requests

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()
# Configura a chave de API da OpenAI
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Função para pré-processar um PDF carregado
async def preprocess_pdf(pdf_content):
    # Salva o conteúdo do PDF em um arquivo temporário
    with open("temp.pdf", "wb") as f:
        f.write(pdf_content)
    # Lê o arquivo PDF
    pdf_reader = PdfReader("temp.pdf")
    text = ""
    # Extrai o texto de cada página do PDF
    for page in pdf_reader.pages:
        text += page.extract_text() or ''

    # Divide o texto em pedaços para processamento
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text=text)
    return chunks

# Função para gerar uma resposta com base na consulta
async def generate_response(query, VectorStore):
    start_time = time.time()  # Inicia a contagem do tempo

    # Busca documentos similares à consulta
    docs = VectorStore.similarity_search(query=query, k=3)

    # Configura o modelo de linguagem da OpenAI
    llm = ChatOpenAI(model_name='gpt-3.5-turbo')

    # Carrega a cadeia de questionamento e resposta
    chain = load_qa_chain(llm=llm, chain_type="stuff")
    with get_openai_callback() as cb:
        # Executa a cadeia e obtém a resposta
        response = chain.run(input_documents=docs, question=query)
        # Imprime informações sobre o uso de tokens
        print(f"Número total de tokens utilizados: {cb.total_tokens}")
        print(f"Custo estimado: {cb.total_cost}")

    end_time = time.time()   # Termina a contagem do tempo
    print(f"Tempo total para processar a resposta: {end_time - start_time} seconds")
    
    response_url = "http://localhost:5000/"
    audio_response = requests.get(response_url, params={'text': response}).content

    # Return both text and audio responses
    return response, audio_response

# Função para iniciar o chat
@cl.on_chat_start
async def on_chat_start():
    files = None
    # Aguarda o usuário fazer upload de um arquivo PDF
    while files is None:
        files = await cl.AskFileMessage(
            content="Por favor, faça o upload do seu PDF!", accept=["application/pdf"]
        ).send()

    # Processa o arquivo PDF carregado
    pdf_file = files[0]
    chunks = await preprocess_pdf(pdf_file.content)
    # Salva os pedaços do texto e o nome do arquivo na sessão do usuário
    store_name = pdf_file.name.split('.')[0]
    cl.user_session.set("chunks", chunks)
    cl.user_session.set("store_name", store_name)

    # Envia mensagem de confirmação de carregamento do arquivo
    await cl.Message(content=f"`{pdf_file.name}` carregado com sucesso. Agora você pode fazer perguntas!").send()

# Função principal para responder mensagens
@cl.on_message
async def main(message):
    query = message.content
    # Obtém os pedaços do texto e o nome do arquivo da sessão do usuário
    chunks = cl.user_session.get("chunks")
    store_name = cl.user_session.get("store_name")

    # Verifica se o PDF foi carregado e processado
    if chunks and store_name:

        # Carrega ou cria um VectorStore
        if os.path.exists(f"{store_name}.pkl"):
            with open(f"{store_name}.pkl", "rb") as f:
                VectorStore = pickle.load(f)
        else:
            embeddings = OpenAIEmbeddings()
            VectorStore = FAISS.from_texts(chunks, embedding=embeddings)
            with open(f"{store_name}.pkl", "wb") as f:
                pickle.dump(VectorStore, f)
                
        # Gera e envia a resposta
            # n: Call the modified generate_response function
        text_response, audio_response = await generate_response(query, VectorStore)

        # n: Sending the audio response as a file
        # n: In Chainlit, you may need to adjust how audio data is sent to the client
        elements = [cl.Audio(name="resposta", display="inline", content=audio_response)]
        
        # n: Send both text and audio responses
        text_message = cl.Message(elements=elements, content=text_response)
        await text_message.send()
    else:
        prompt_message = cl.Message(content="Por favor, faça o upload do seu PDF!")
        await prompt_message.send()

if __name__ == '__main__':
    cl.run()

