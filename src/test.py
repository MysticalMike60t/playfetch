import re

from playwright.sync_api import sync_playwright

import scrape
import validation
from regex import EMAIL_RE


def main():
    print(validation.clean_domain("0.0.0.0:8743"))
    print(validation.clean_domain("www.python.org"))
    html = scrape.pull("http://127.0.0.1:8743/tests/simple.html")
    # print(html)
    # emails = re.findall(r"html", html)
    # print(emails)
    found_emails = list(
        dict.fromkeys(e.group().lower() for e in EMAIL_RE.finditer(html))
    )
    for email in found_emails:
        print(email)
