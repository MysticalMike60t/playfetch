from bs4 import BeautifulSoup
from prompt_toolkit import HTML, print_formatted_text
from prompt_toolkit.shortcuts import ProgressBar

import config
from regex import EMAIL_RE


def navigation(soup: BeautifulSoup):
    print("Running email analysis")
    emails(soup.text)


def emails(html: str):
    print("Starting emails analysis")
    emails = list(dict.fromkeys(e.group().lower() for e in EMAIL_RE.finditer(html)))
    print_formatted_text(
        HTML(f'<style fg="{config.Theme.text_muted}">Finished Regex</style>')
    )
    with open(config.Paths.datafile, "a") as datafile:
        datafile.writelines("\n")
        print("Wrote line to datafile")
        print("Beginning to write emails to datafile")
        with ProgressBar() as pb:
            for email in pb(emails, label="Writing emails to datafile"):
                datafile.writelines(str(email))
                print(f"Wrote email: {str(email)}")
    print("Finished emails analysis")
