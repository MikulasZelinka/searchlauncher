import webbrowser
from string import Template
from urllib.parse import quote

from loguru import logger

from searchlauncher.settings import load_settings


def open_in_browser(query: str, group_name: str | None) -> None:
    group_name = group_name or "all"

    logger.info(f"Opening search for '{query}', group '{group_name}'")
    query = quote(query, safe="")
    logger.debug(f"Encoded query: '{query}'")

    settings = load_settings()

    # a group can also include other groups
    groups = [group_name] + settings.groups[group_name].groups
    # sites = {
    #     name: url for name, url in settings.sites.items()
    #     if any(name in settings.groups[g].sites for g in groups)
    # }

    sites = (
        dict(
            filter(
                lambda name_url: any(name_url[0] in settings.groups[g].sites for g in groups), settings.sites.items()
            )
        )
        if group_name != "all"
        else settings.sites
    )

    for name, template in sites.items():
        url = Template(template).substitute(query=query)
        logger.debug(f"Site '{name}', url: {url}")
        webbrowser.open(url)

    logger.success("All searches opened")
