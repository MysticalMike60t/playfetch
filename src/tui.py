import os
import subprocess

import questionary as q

import config


def tclear():
    subprocess.run("cls||clear", shell=True)


def seperator(symbol: str = "-"):
    twidth = os.get_terminal_size()[0]
    ending = "\n" if (len(symbol) % twidth) else ""
    print(symbol * twidth, end=ending)


def cseperator(symbol: str = "-"):

    twidth = os.get_terminal_size()[0]
    ending = "\n" if (len(symbol) % twidth) else ""
    q.print(symbol * twidth, end=ending, style=f"fg:{config.Theme.accent_muted_hex}")
