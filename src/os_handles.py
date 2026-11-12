import sys
from pathlib import Path


# I only have this so I can ensure a graceful shutdown
def quit(code: int = 0, type: str = "safe"):
    match type:
        case "safe":
            sys.exit(code)
        case _:
            sys.exit(code)


def app_dir() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parent
