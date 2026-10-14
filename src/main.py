import sys

import requests
from handles import HandleStatusCode


def main() -> int:
    inputs = {"domain": input("Domain: "), "path": input("Path: ")}
    res = requests.get_page(inputs["domain"], inputs["path"])
    HandleStatusCode().print(res.status)
    return 0


if __name__ == "__main__":
    sys.exit(main())
