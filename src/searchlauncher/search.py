import webbrowser
from string import Template
from urllib.parse import quote

from loguru import logger

TEMPLATES = {
    "aukro": "https://aukro.cz/vysledky-vyhledavani?text=$query",
    "sbazar": "https://www.sbazar.cz/hledej/$query",
    "bazos": "https://www.bazos.cz/search.php?hledat=$query",
    "marketplace": "https://www.facebook.com/marketplace/search/?query=$query",
    "zbozi": "https://www.zbozi.cz/hledej/?q=$query&razeni=nejlevnejsi",
    "heureka": "https://www.heureka.cz/?h%5Bfraze%5D=$query&o=3",
}


def open_in_browser(query: str) -> None:
    logger.info(f"Opening search for '{query}'")
    query = quote(query, safe="")
    logger.debug(f"Encoded query: '{query}'")

    for name, template in TEMPLATES.items():
        url = Template(template).substitute(query=query)
        logger.debug(f"Provider '{name}', query: {url}")
        webbrowser.open(url)

    logger.success("All searches opened")
