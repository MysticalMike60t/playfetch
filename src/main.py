import os
import sys

import requests
from handles import HandleStatusCode

# IDEA: Gets ALL information useful to OSINT. Not just from a single platform, and also
# not just a google search.

# IDEA: Also include email, name, etc. inputs.

# IDEA: Checks business or other official records hosted places for names in domain,
# or inside of the page's main/branding elements detected by algorithm.


def main() -> int:
    inputs = {"domain": input("Domain: "), "path": input("Path: ")}
    res = requests.get_page(inputs["domain"], inputs["path"])
    HandleStatusCode().print(res.status)
    return 0


if __name__ == "__main__":
    try:  # Pray
        sys.exit(main())
    except KeyboardInterrupt:  # Prayer wasn't answered :(
        # Be sad that the person interrupted this perfection
        # Also make it red to show the sadness you caused
        print(  # Scary ANSI escape mumbo-jumbo
            "\r\x1b[K\x1b[31mYou killed me :(\x1b[0m", file=sys.stderr
        )
        try:
            sys.exit(130)
        except SystemExit:
            # If system won't exit, be a Karen and go to its manager to yell at it
            os._exit(130)
