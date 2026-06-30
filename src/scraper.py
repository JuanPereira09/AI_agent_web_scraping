from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def obter_texto_da_pagina(url: str) -> str:
    """
    Abre um navegador real em segundo plano usando Playwright,
    espera a página carregar e limpa o HTML para o Agente de IA.
    """
    try:
        with sync_playwright() as p:
            # Lança o navegador Chromium em modo oculto (headless=True)
            browser = p.chromium.launch(headless=True)
            
            # Cria um contexto simulando um navegador comum para evitar bloqueios
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                viewport={"width": 1280, "height": 720}
            )
            
            page = context.new_page()
            
            # Navega até a URL e espera até que a rede esteja ociosa (carregamento completo)
            page.goto(url, wait_until="networkidle", timeout=30000)
            
            # Captura o HTML completo renderizado
            html_conteudo = page.content()
            browser.close()
            
        # Limpeza do HTML com BeautifulSoup (igual ao anterior)
        soup = BeautifulSoup(html_conteudo, "html.parser")
        
        for elemento in soup(["script", "style", "nav", "footer", "header", "noscript"]):
            elemento.decompose()
            
        texto_limpo = soup.get_text(separator="\n")
        linhas = [linha.strip() for list_linha in texto_limpo.splitlines() if (linha := list_linha.strip())]
        
        return "\n".join(linhas)
        
    except Exception as e:
        return f"Erro ao acessar a URL com Playwright: {e}"