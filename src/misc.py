# Shit I don't know where else it should go
# or it just doesn't fit anywhere else

import io
import random

from bs4 import BeautifulSoup as BS  # Ha ha, funny name :3


def parse_html(raw_html) -> BS:
    soup = BS(raw_html, "lxml")
    return soup


def extract_links(soup: BS):
    links: list[str] = []
    for link in soup.select("a[href]"):
        links.extend(link["href"])
    return links


def write_links_list(links_list: list[str]):
    fname: str = str(random.getrandbits(32))
    links: list[str] = []
    for link in links_list:
        links.append(rf"{link}\n")
    with open(f"{fname}", "w") as f:
        for link in links:
            f.write(link)
        f.close()
