__version__ = "0.0-alpha.1"

import os
import random
import subprocess
import sys
from datetime import datetime

import questionary as q
import requests
from art import text2art
from bs4 import BeautifulSoup

import analyze
import config
import os_handles
import search
import tui
from validation import clean_for_path

# IDEA: Gets ALL information useful to OSINT. Not just from a single platform, and also
# not just a google search.

# IDEA: Also include email, name, phone number, etc. inputs.

# IDEA: Input can be a profile. Basically every option mentioned above,
# but also including business name, address, social media handles, etc.

# IDEA: Checks business or other official records hosted places for names in domain,
# or inside of the page's main/branding elements detected by algorithm.

# NEED TO ADD: Check if binary is inside of bin or PATH directory. Then, determine where generated files go.


def init_head():
    tui.tclear()
    ascii_art = text2art("PlayFetch", "alligator3")
    q.print(f"{ascii_art}", style=f"fg:{config.Theme.accent_hex}")
    q.print(f"{__version__}\n", style=f"fg:{config.Theme.text_muted}")
    q.print("By: Caden Finkelstein", style=f"fg:{config.Theme.accent_dark_hex}")
    q.print(
        "\nThis is in early alpha development, and has a lot of issues.",
        style=f"bold fg:{config.Theme.status_fg} bg:{config.Theme.status_bg}",
    )
    tui.cseperator()
    print()


def handle_search():
    search_type: str = q.select(
        "Select search type:",
        choices=[
            "Email",
            "Username",
            "Name",
            "Phone Number",
            "Domain",
            "Quit",
        ],
    ).ask()
    if search_type == "Quit":
        os_handles.quit(0)
    search_filter: str = q.text(f"Enter the {search_type.lower()}:").ask()
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    dump_path = f"{config.Paths.cwd}/{timestamp}_{clean_for_path(search_filter)}"
    if not os.path.exists(dump_path):
        os.mkdir(dump_path)
    # q.print(
    #     f"Current working directory (after switching to dump_path): {config.Paths.cwd}",
    #     f"fg:{config.Theme.debug_fg}",
    # )
    config.Paths.cwd = f"{dump_path}"
    config.Paths.datafile = (
        f"{dump_path}/{random.randrange(100000, 999999)}_{search_filter}"
    )
    # q.print(
    #     f"Current datafile path: {config.Paths.datafile}", f"fg:{config.Theme.debug_fg}"
    # )
    with open(config.Paths.datafile, "a") as datafile:
        datafile.writelines(
            [
                f"Search Type: {search_type}\n",
                f"Filter (search query): {search_filter}\n",
            ]
        )
        # q.print("Done writing inputs to datafile", f"fg:{config.Theme.debug_fg}")
    # q.print("Starting search", f"fg:{config.Theme.debug_fg}")
    if q.confirm(f"Search duckduckgo for {search_filter}?").ask():
        tui.cseperator()
        results = search.ddg(search_filter, type="email")
    else:
        return
    if not results:
        q.print(
            "No results (likely blocked/rate-limited)", f"fg:{config.Theme.error_fg}"
        )
    with open(config.Paths.datafile, "a") as datafile:
        for url in results:
            datafile.writelines(f"{url}\n")
            q.print(f">\t{url}", f"italic fg:{config.Theme.output_fg}")
    # q.print("Done searching", f"fg:{config.Theme.debug_fg}")


def main() -> int:
    while True:
        init_head()
        if not os.path.exists(config.Paths.datadump):
            os.mkdir(config.Paths.datadump)
        config.Paths.cwd = f"{config.Paths.datadump}"
        # q.print(
        #     f"Current working directory: {config.Paths.cwd}", f"fg:{config.Theme.debug_fg}"
        # )
        handle_search()
        if not q.confirm("Go back?").ask():
            break
    # q.print("Done", f"fg:{config.Theme.debug_fg}")

    # inputs = {"domain": input("Domain: "), "path": input("Path (without first '/'): ")}
    # config.Paths.cwd = f"{config.Paths.datadump}"
    # print(f"Current working directory: {config.Paths.cwd}")
    # timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    # cleaned_domain = inputs["domain"].replace(".", "_")
    # dump_path = f"{config.Paths.cwd}/{timestamp}_{cleaned_domain}"
    # print(f"Current dump directory: {dump_path}")
    # config.Paths.cwd = f"{dump_path}"
    # if not os.path.exists(dump_path):
    #     os.mkdir(dump_path)
    # print(
    #     f"Current working directory (after switching to dump_path): {config.Paths.cwd}"
    # )
    # config.Paths.datafile = (
    #     f"{dump_path}/{random.randrange(100000, 999999)}_{cleaned_domain}"
    # )
    # print(f"Current datafile path: {config.Paths.datafile}")
    # with open(config.Paths.datafile, "a") as datafile:
    #     datafile.writelines(
    #         [
    #             "User input:\n",
    #             f"\tDomain: {inputs['domain']}\n",
    #             f"\tPath: {inputs['path']}\n",
    #             "\n",
    #         ]
    #     )
    #     print("Wrote domain and path to datafile")
    # res = requests.get(
    #     f"http://{inputs['domain']}/{inputs['path']}"
    # )  # Add validation and ask if HTTPS (defaults to yes)
    # print("Finished HTTP/HTTPS request")
    # soup = BeautifulSoup(res.content, "html.parser")
    # print("Created soup")
    # print("Starting analysis")
    # analyze.navigation(soup)
    # print("Finished analysis")
    return 0


if __name__ == "__main__":
    try:  # Pray
        os_handles.quit(main())
    except KeyboardInterrupt:  # Prayer wasn't answered :(
        # Be sad that the person interrupted this perfection
        # Also make it red to show the sadness you caused
        print(  # Scary ANSI escape mumbo-jumbo
            "\r\x1b[K\x1b[31mYou killed me :(\x1b[0m", file=sys.stderr
        )
        try:
            os_handles.quit(130)
        except SystemExit:
            # If system won't exit, be a Karen and go to its manager to yell at it
            os._exit(130)
