import sys


# I only have this so I can ensure a graceful shutdown
def quit(code: int = 0, type: str = "safe"):
    match type:
        case "safe":
            sys.exit(code)
        case _:
            sys.exit(code)
