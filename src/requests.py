import http.client as http

import validate


def get_page(host_domain: str, url_path: str) -> http.HTTPResponse:
    domain: str = validate.domain(host_domain)
    path: str = validate.path(url_path)

    conn = http.HTTPSConnection(domain)
    conn.request("GET", path)
    res = conn.getresponse()
    return res
