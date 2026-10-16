import logging
import os
import sys

import decode
import parse
import requests
from config import CONFIG
from handles import HandleStatusCode
from log import log

# IDEA: Gets ALL information useful to OSINT. Not just from a single platform, and also
# not just a google search.

# IDEA: Also include email, name, phone number, etc. inputs.

# IDEA: Input can be a profile. Basically every option mentioned above,
# but also including business name, address, social media handles, etc.

# IDEA: Checks business or other official records hosted places for names in domain,
# or inside of the page's main/branding elements detected by algorithm.

logger = logging.getLogger(__name__)
logging.basicConfig(filename=f"{CONFIG.paths.logs}/{__name__}.log", level=logging.DEBUG)


def main() -> int:
    inputs = {"domain": input("Domain: "), "path": input("Path: ")}
    res = requests.get_page(inputs["domain"], inputs["path"])
    if __debug__:
        log(f"{CONFIG.session.id}_request-response").debug(res)
        log(f"{CONFIG.session.id}_request-response").debug(res.status)
    HandleStatusCode().print(res.status)
    html = decode.http_res_content_compression(res)  # Add type defs
    parse.html(html)
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
