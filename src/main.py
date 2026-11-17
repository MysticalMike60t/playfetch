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
import scrape
import search
import tui
from config import Instances, Theme
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
    q.print(f"{ascii_art}", style=f"fg:{Theme.accent_hex}")
    q.print(f"{config.__version_tag__}\n", style=f"fg:{Theme.text_muted}")
    q.print("By: Caden Finkelstein", style=f"fg:{Theme.accent_dark_hex}")
    q.print(
        "\nSTATUS\tThis is in early alpha development, and has a lot of issues.",
        style=f"bold fg:{Theme.status_fg} bg:{Theme.status_bg}",
    )
    tui.cseperator()
    q.print(
        "WARNING\tOnly email search type is implemented. Others just search via query with no analysis.",
        f"fg:{Theme.warning_fg}",
    )
    print()


def handle_search():
    SEARCH_TYPES = {
        "Any": "any",
        "Email": "email",
        "Username": "username",
        "Name": "name",
        "Phone Number": "phone",
        "Domain": "domain",
    }

    search_type = (
        tui.qselect("Select search type:", choices=[*SEARCH_TYPES, "Quit"]) or "Quit"
    )
    if search_type == "Quit":
        os_handles.quit(0)

    query = q.text(f"Enter {search_type.lower()}:").ask()
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    dump_path = f"{config.Paths.cwd}/{timestamp}_{clean_for_path(query)}"
    if not os.path.exists(dump_path):
        os.mkdir(dump_path)
    # q.print(
    #     f"Current working directory (after switching to dump_path): {config.Paths.cwd}",
    #     f"fg:{Theme.debug_fg}",
    # )
    config.Paths.cwd = f"{dump_path}"
    config.Paths.datafile = f"{dump_path}/{random.randrange(100000, 999999)}_{query}"
    # q.print(
    #     f"Current datafile path: {config.Paths.datafile}", f"fg:{Theme.debug_fg}"
    # )
    with open(config.Paths.datafile, "a") as datafile:
        datafile.writelines(
            [
                f"Search Type: {search_type}\n",
                f"Filter (search query): {query}\n",
            ]
        )
        # q.print("Done writing inputs to datafile", f"fg:{Theme.debug_fg}")
    # q.print("Starting search", f"fg:{Theme.debug_fg}")
    q.print(
        "You may get rate-limited, which will fail to return any results.",
        style=f"fg:{Theme.warning_fg}",
    )
    if q.confirm(f"Search duckduckgo for {query}?").ask():
        tui.cseperator()
        num_results: int = 20
        match search_type:
            case "Any":
                results: list[str] = search.ddg(
                    query, type=SEARCH_TYPES["Any"], n=num_results
                )
                if results.__len__() == 0:
                    return
            case "Email":
                results: list[str] = search.ddg(
                    query, type=SEARCH_TYPES["Email"], n=num_results
                )
                if results.__len__() == 0:
                    return
            case _:
                results: list[str] = []
                q.print("No search type selection made.", f"fg:{Theme.error_fg}")
                if results.__len__() == 0:
                    return

    else:
        return
    with open(config.Paths.datafile, "a") as datafile:
        for url in results:
            datafile.writelines(f"{url}\n")
            q.print(f">\t{url}", f"italic fg:{Theme.output_fg}")
    # q.print("Done searching", f"fg:{Theme.debug_fg}")
    if q.confirm("Scrape these pages for data (n will skip to next result)?").ask():
        match q.select(
            "Search these pages for:",
            choices=["Emails", "URLs"],
            style=Theme.Questionary,
            pointer=Theme.questionary_select_pointer,
        ).ask():
            case "Emails":
                for result in results:
                    try:
                        q.print(
                            f"Scraping {result} for emails...", f"fg:{Theme.info_fg}"
                        )
                        html = scrape.pull(result)
                        analyze.emails(html)
                    except Exception as e:
                        q.print(
                            f'Failed scraping "{result}", Unsupported result',
                            f"fg:{Theme.error_fg}",
                        )

            case "URLs":
                for result in results:
                    q.print(f"Scraping {result}", f"fg:{Theme.info_fg}")
                    try:
                        html = scrape.pull(result)  # cause of url crash
                        urls_list = analyze.urls(html, True) or list()
                        if q.confirm("Scrape these pages for emails?").ask():
                            for url in urls_list:
                                try:
                                    q.print(
                                        f"Scraping {url} for emails...",
                                        f"fg:{Theme.info_fg}",
                                    )
                                    html = scrape.pull(url)
                                    analyze.emails(html)
                                except Exception as e:
                                    q.print(
                                        f'Failed scraping "{url}", Unsupported URL\n{e}',
                                        f"fg:{Theme.error_fg}",
                                    )
                    except Exception as e:
                        q.print(
                            f'Failed scraping "{result}", Unsupported result\n{e}',
                            f"fg:{Theme.error_fg}",
                        )
            case _:
                q.print("No selection made.", f"fg:{Theme.error_fg}")


def main() -> int:
    while True:
        init_head()
        if not os.path.exists(config.Paths.datadump):
            os.mkdir(config.Paths.datadump)
        config.Paths.cwd = f"{config.Paths.datadump}"
        # q.print(
        #     f"Current working directory: {config.Paths.cwd}", f"fg:{Theme.debug_fg}"
        # )
        handle_search()
        if not q.confirm("Go back?").ask():
            break
    # q.print("Done", f"fg:{Theme.debug_fg}")
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
