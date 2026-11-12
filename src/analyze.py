from config import Instances, Paths, Theme
from regex import EMAIL_RE


def emails(html: str):
    emails = list(dict.fromkeys(e.group().lower() for e in EMAIL_RE.finditer(html)))
    with open(Paths.datafile, "a") as datafile:
        datafile.writelines("\n")
        if emails.__len__() >= 1:
            for email in emails:
                datafile.writelines(str(email))
                print(f"Found {Instances.term.color_hex(Theme.accent_hex)(email)}")
