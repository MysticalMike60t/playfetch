# Shit I don't know where else it should go
# or it just doesn't fit anywhere else

import random

from bs4 import BeautifulSoup as BS

from config import CONFIG
from log import log


def extract_links(soup: BS):  # Add type defs
    links: list[str] = []
    for link in soup.select("a[href]"):
        links.extend(link["href"])
    return links


def write_links_list(links_list: list[str]):  # Add type defs
    fname: str = str(random.getrandbits(32))
    links: list[str] = []
    for link in links_list:
        links.append(rf"{link}\n")
        if __debug__:
            log(f"{CONFIG.session.id}_links-list").debug(link)
            log(f"{CONFIG.session.id}_links-list").debug(links)
    with open(f"{fname}", "w") as f:
        for link in links:
            f.write(link)
            if __debug__:
                log(f"{CONFIG.session.id}_links-list_file").debug(link)
                log(f"{CONFIG.session.id}_links-list_file").debug(links)
        f.close()
