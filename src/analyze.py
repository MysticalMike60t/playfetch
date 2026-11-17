from config import Instances, Paths, Theme
from regex import EMAIL_RE, URL_RE


def _log(found: list[str]):
    with open(Paths.datafile, "a") as datafile:
        datafile.write("\n")
        for item in found:
            datafile.write(f"{item}\n")
            print(f"Found {Instances.term.color_hex(Theme.accent_hex)(item)}")


def emails(html: str):
    _log(list(dict.fromkeys(e.group().lower() for e in EMAIL_RE.finditer(html))))


def urls(html: str, returnList: bool = False):
    if not returnList:
        _log(
            list(
                dict.fromkeys(
                    u.group().rstrip(".,;:!?)]}") for u in URL_RE.finditer(html)
                )
            )
        )
    else:
        urls_list = list(
            dict.fromkeys(u.group().rstrip(".,;:!?)]}") for u in URL_RE.finditer(html))
        )
        _log(urls_list)
        return urls_list
