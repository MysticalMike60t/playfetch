import pathlib
from dataclasses import dataclass, field


@dataclass
class Paths:
    cwd: str = str(pathlib.Path().absolute())
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
