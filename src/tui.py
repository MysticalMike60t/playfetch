import os
import subprocess

import questionary as q

from config import Instances, Theme


def tclear():
    subprocess.run("cls||clear", shell=True)


def seperator(symbol: str = "-"):
    twidth = os.get_terminal_size()[0]
    ending = "\n" if (len(symbol) % twidth) else ""
    print(symbol * twidth, end=ending)


def cseperator(symbol: str = "-"):
    twidth = os.get_terminal_size()[0]
    ending = "\n" if (len(symbol) % twidth) else ""
    q.print(symbol * twidth, end=ending, style=f"fg:{Theme.accent_muted_hex}")


def qselect(message: str, choices: list[str]) -> str:
    return q.select(
        message,
        choices=choices,
        style=Theme.Questionary,
        pointer=Theme.questionary_select_pointer,
        instruction="(Use Arrow Keys)",
    ).ask()
