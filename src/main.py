import os
import random
import sys
from datetime import datetime

import requests
from bs4 import BeautifulSoup

import analyze
import config

# IDEA: Gets ALL information useful to OSINT. Not just from a single platform, and also
# not just a google search.

# IDEA: Also include email, name, phone number, etc. inputs.

# IDEA: Input can be a profile. Basically every option mentioned above,
# but also including business name, address, social media handles, etc.

# IDEA: Checks business or other official records hosted places for names in domain,
# or inside of the page's main/branding elements detected by algorithm.


def main() -> int:
    if not os.path.exists(config.Paths.datadump):
        os.mkdir(config.Paths.datadump)
    inputs = {"domain": input("Domain: "), "path": input("Path (without first '/'): ")}
    config.Paths.cwd = f"{config.Paths.datadump}"
    print(f"Current working directory: {config.Paths.cwd}")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    cleaned_domain = inputs["domain"].replace(".", "_")
    dump_path = f"{config.Paths.cwd}/{timestamp}_{cleaned_domain}"
    print(f"Current dump directory: {dump_path}")
    config.Paths.cwd = f"{dump_path}"
    if not os.path.exists(dump_path):
        os.mkdir(dump_path)
    print(
        f"Current working directory (after switching to dump_path): {config.Paths.cwd}"
    )
    config.Paths.datafile = (
        f"{dump_path}/{random.randrange(100000, 999999)}_{cleaned_domain}"
    )
    print(f"Current datafile path: {config.Paths.datafile}")
    with open(config.Paths.datafile, "a") as datafile:
        datafile.writelines(
            [
                "User input:\n",
                f"\tDomain: {inputs['domain']}\n",
                f"\tPath: {inputs['path']}\n",
                "\n",
            ]
        )
        print("Wrote domain and path to datafile")
    res = requests.get(
        f"http://{inputs['domain']}/{inputs['path']}"
    )  # Add validation and ask if HTTPS (defaults to yes)
    print("Finished HTTP/HTTPS request")
    soup = BeautifulSoup(res.content, "html.parser")
    print("Created soup")
    print("Starting analysis")
    analyze.navigation(soup)
    print("Finished analysis")
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
