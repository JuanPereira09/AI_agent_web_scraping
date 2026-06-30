import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from google import genai
from google.genai import types

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# 1. Definimos o esquema de dados que queremos extrair usando Pydantic
class DetalhesProduto(BaseModel):
    nome: str = Field(description="O nome completo do produto encontrado na página.")
    preco_atual: float = Field(description="O preço atual do produto em formato decimal/float. Se não encontrado ou indisponível, retorne 0.0.")
    moeda: str = Field(description="A moeda do preço (ex: BRL, USD).")
    disponivel: bool = Field(description="True se o produto estiver em estoque e disponível para compra, False caso contrário.")
    tags_caracteristicas: list[str] = Field(description="Uma lista com até 5 características principais do produto (ex: '8GB RAM', 'Cor Preto').")

def analisar_dados_produto(texto_pagina: str) -> DetalhesProduto:
    """
    Envia o texto limpo da página para o Gemini e força o retorno
    estruturado conforme a classe DetalhesProduto.
    """
    # Inicializa o cliente do Gemini usando a chave do .env
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    
    prompt = f"""
    Você é um agente especialista em Web Scraping e Análise de Dados de E-commerce.
    Analise o texto extraído de uma página de produto abaixo e extraia com precisão as informações solicitadas.
    
    Texto da página:
    ---
    {texto_pagina}
    ---
    """
    
    # Fazemos a chamada solicitando uma resposta estruturada (JSON Schema)
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=DetalhesProduto,
            temperature=0.1, # Temperatura baixa para a IA ser mais factual e precisa
        ),
    )
    
    # Retorna os dados mapeados automaticamente para o nosso objeto Pydantic
    return DetalhesProduto.model_validate_json(response.text)