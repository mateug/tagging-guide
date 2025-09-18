from firecrawl import Firecrawl


def scrape_url(url: str, api_key: str) -> dict:
    """
    Realiza scraping de la URL usando Firecrawler y devuelve el resultado como dict.
    """
    crawler = Firecrawl(api_key = api_key)
    result = crawler.scrape(
        url,
        formats=[
            "markdown",
            "summary",
            "html",
            "rawHtml",
            {"type": "screenshot", "fullPage": True}
        ]
    )
    return result


def get_html(result: dict) -> str:
    """
    Extrae el HTML del resultado del scraping.
    """
    return getattr(result, "html", "No se encontró HTML")

def get_summary(result: dict) -> str:
    """
    Extrae el summary del resultado del scraping.
    """
    return getattr(result, "summary", "No se encontró summary")

def get_markdown(result: dict) -> str:
    """
    Extrae el markdown del resultado del scraping.
    """
    return getattr(result, "markdown", "No se encontró markdown")

def get_screenshot(result: dict):
    """
    Extrae la captura de pantalla del resultado del scraping.
    """
    return getattr(result, "screenshot", "No se encontró screenshot")

def get_json(result: dict) -> dict:
    """
    Devuelve el resultado completo en formato JSON.
    """
    return result.json() if hasattr(result, "json") else {}
