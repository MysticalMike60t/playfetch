from dataclasses import dataclass, field
from importlib.metadata import PackageNotFoundError, version

import questionary as q
from blessed import Terminal

import os_handles

try:
    __version_raw__ = version("playfetch").removeprefix("v")
    __version__ = __version_raw__  # Only included in case it is needed
    __version_tag__ = f"v{__version_raw__}"
    __version_title__ = f"Release Build {__version_tag__}"
except PackageNotFoundError:
    __version__ = "x.x.x+unknown"


@dataclass
class Paths:
    cwd: str = str(os_handles.app_dir())
    datafile: str = field(default=f"{cwd}/.datafile")
    datadump: str = field(default=f"{cwd}/.datadump")


@dataclass
class Theme:
    accent_hex: str = "#8ECF23"
    accent_dark_hex: str = "#608522"
    accent_muted_hex: str = "#2E382A"
    bg_hex: str = "#30362C"
    info_fg: str = "#65ADFC"
    debug_fg: str = "#CB95F0"
    status_fg: str = "#E8D409"
    status_bg: str = "#2B2701"
    warning_fg: str = "#FCB865"
    error_fg: str = "#FC6565"
    success_fg: str = "#65FC6A"
    output_fg: str = "#65FCF9"
    text_muted: str = "#313131"
    questionary_select_pointer: str = "►"
    Questionary: q.Style = q.Style(
        [
            ("qmark", f"fg:{accent_hex}"),
            ("question", "bold"),
            ("answer", f"fg:{accent_hex} bold"),
            (
                "pointer",
                f"fg:{accent_hex} bold",
            ),
            (
                "highlighted",
                f"fg:{accent_hex} bold",
            ),
            ("selected", "fg:#cc5454"),
            ("separator", "fg:#cc5454"),
            ("instruction", ""),
            ("text", ""),
            (
                "disabled",
                f"fg:{text_muted} italic",
            ),
        ]
    )


class Instances:
    term: Terminal = Terminal()
