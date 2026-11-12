import questionary as q
from ddgs import DDGS

import config


def ddg(query: str, type: str = "", n: int = 10) -> list[str]:
    match type.lower():
        case "email":
            try:
                results = DDGS().text(query, max_results=n)
            except Exception as e:
                q.print(f"Search failed: {e}", f"fg:{config.Theme.error_fg}")
                return []
            return [r["href"] for r in results]
        case _:
            q.print(
                "Un-implemented type or no selection made.",
                f"fg:{config.Theme.error_fg}",
            )
            return []
