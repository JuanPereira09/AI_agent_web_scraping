# 🕵️‍♂️ Intelligent AI Web Scraper & Data Structurer

Um agente de Inteligência Artificial especializado em Web Scraping resiliente e estruturação autônoma de dados de e-commerce. O projeto utiliza **Python**, **Playwright** e o modelo **Gemini 2.5** via técnicas avançadas de **Structured Outputs** (Saídas Estruturadas) orientadas por contratos de dados do **Pydantic**.

## 🚀 O Problema que este projeto resolve
Scrapers tradicionais construídos apenas com seletores CSS fixos ou Expressões Regulares (Regex) são frágeis. Qualquer alteração boba no layout do site alvo (mudança de uma classe, ID ou organização de tags) quebra o pipeline de dados da empresa.

Este projeto resolve o problema de resiliência unindo o **Playwright** para renderização dinâmica de páginas com o poder cognitivo do **Gemini 2.5-Flash**. Em vez de buscar por tags específicas, a IA interpreta o conteúdo textual bruto da página e extrai os dados mapeando-os diretamente para um modelo estritamente tipado, garantindo robustez contra mudanças de design do site.

## 🛠️ Tecnologias Utilizadas
- **Python 3.11+**
- **Google GenAI SDK** (Modelo `gemini-2.5-flash`)
- **Pydantic** (Validação de tipos e garantia de esquema JSON estável)
- **Playwright** (Navegação automárica e renderização de JavaScript em segundo plano)
- **BeautifulSoup4** (Limpeza e otimização de tokens do HTML bruto)
- **Python-dotenv** (Gerenciamento seguro de credenciais)

## 🏗️ Arquitetura do Sistema
- `src/scraper.py`: Instancia o navegador headless, aguarda o carregamento total dos scripts e extrai o texto visível.
- `src/agent.py`: Define o contrato de dados com Pydantic e orquestra a chamada do Gemini forçando o retorno estruturado (`response_schema`).
- `src/main.py`: Ponto de entrada que centraliza o fluxo e exibe o output limpo.

## 📊 Exemplo de Saída Estruturada (JSON Schema)
Independentemente da complexidade visual ou do idioma original da plataforma, o agente normaliza os dados perfeitamente:

```json
{
    "nome": "Asus VivoBook X441NA-GA190 Chocolate Black",
    "preco_atual": 295.99,
    "moeda": "USD",
    "disponivel": true,
    "tags_caracteristicas": [
        "14\"",
        "Celeron N3450",
        "4GB",
        "128GB SSD",
        "Endless OS"
    ]
}
