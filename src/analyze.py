from bs4 import BeautifulSoup

import config
from regex import EMAIL_RE


def navigation(soup: BeautifulSoup):
    print("Running email analysis")
    emails(soup.text)


def emails(blob: str):
    print("Starting emails analysis")
    emails = EMAIL_RE.findall(blob)
    print("Finished Regex")
    with open(config.Paths.datafile, "a") as datafile:
        datafile.writelines("\n")
        print("Wrote line to datafile")
        print("Beginning to write emails to datafile")
        for email in emails:
            datafile.writelines(str(email))
            print(f"Wrote email: {str(email)}")
    print("Finished emails analysis")
