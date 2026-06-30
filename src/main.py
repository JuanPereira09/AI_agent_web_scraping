import json
from scraper import obter_texto_da_pagina
from agent import analisar_dados_produto

def rodar_agente(url: str):
    print(f"🕵️‍♂️ Iniciando extração da URL: {url}\n")
    
    # Passo 1: Captura o texto do e-commerce
    print("⏳ Baixando e limpando o HTML da página...")
    texto_bruto = obter_texto_da_pagina(url)
    
    if texto_bruto.startswith("Erro ao acessar"):
        print(f"❌ {texto_bruto}")
        return

    # Passo 2: Processa o texto com o Agente de IA
    print("🤖 Agente de IA analisando o conteúdo e estruturando os dados...")
    try:
        dados_finais = analisar_dados_produto(texto_bruto)
        
        print("\n🚀 [Resultado do Agente] Dados extraídos com sucesso:")
        # Exibe o resultado formatado como JSON bonitinho na tela
        print(json.dumps(dados_finais.model_dump(), indent=4, ensure_ascii=False))
        
    except Exception as e:
        print(f"❌ Erro durante a análise da IA: {e}")

if __name__ == "__main__":
    # URL de teste aberta para scrapers
    url_teste = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
    
    rodar_agente(url_teste)