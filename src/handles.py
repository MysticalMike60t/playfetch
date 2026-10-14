import http.client as http

from rich.pretty import pprint


# Rename this. Very weird and stupid name you idiot
class HandleStatusCode:
    def print(self, res: http.HTTPResponse | int):
        if isinstance(res, http.HTTPResponse):
            status_code: int = res.status
        else:
            status_code: int = res

        match status_code:
            case 200:
                pprint("200 OK")
            case 301:
                pprint("301")
            case 404:
                pprint("404")
            case _:
                pprint(f"Unknown status code: {status_code}")
