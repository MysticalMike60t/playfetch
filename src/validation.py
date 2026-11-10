import re

from regex import IPV4_ADDR_RE, SUBDOMAIN_WWW_RE


def clean_domain(domain: str) -> str:
    _: str = domain
    while True:
        _ = re.sub(IPV4_ADDR_RE, "localhost_", _)
        _ = re.sub(SUBDOMAIN_WWW_RE, r"\1_\2", _)
        break
    return _
