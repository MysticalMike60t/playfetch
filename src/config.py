import pathlib
from dataclasses import dataclass, field


@dataclass
class Paths:
    cwd: str = str(pathlib.Path().absolute())
    datafile: str = field(default=f"{cwd}/.datafile")
    datadump: str = field(default=f"{cwd}/.datadump")
