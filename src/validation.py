import re

from regex import IPV4_ADDR_RE, SUBDOMAIN_WWW_RE


def clean_domain(domain: str) -> str:
    _: str = domain
    while True:
        _ = re.sub(IPV4_ADDR_RE, "localhost", _)
        _ = re.sub(SUBDOMAIN_WWW_RE, r"\1__\2", _)
        break
    return _


# Basic non-regex cleanup
def clean_for_path(text: str) -> str:
    text = text.replace(" ", "_").replace("\\", "+").replace("/", "+")
    return text
