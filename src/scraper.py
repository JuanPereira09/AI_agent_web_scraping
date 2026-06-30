import requests
from bs4 import BeautifulSoup

def obter_texto_da_pagina(url: str) -> str:
    """
    Faz o download da página web e limpa o HTML, retornando apenas 
    o texto visível para poupar tokens na API de IA.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Remove elementos irrelevantes do HTML que só gastariam memória da IA
        for elemento in soup(["script", "style", "nav", "footer", "header"]):
            elemento.decompose()
            
        # Pega o texto limpo
        texto_limpo = soup.get_text(separator="\n")
        # Remove linhas em branco extras
        linhas = [linha.strip() for list_linha in texto_limpo.splitlines() if (linha := list_linha.strip())]
        
        return "\n".join(linhas)
        
    except Exception as e:
        return f"Erro ao acessar a URL: {e}"