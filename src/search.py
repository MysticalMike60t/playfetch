import questionary
from ddgs import DDGS


def ddg(query: str, type: str = "", n: int = 10) -> list[str]:
    match type.lower():
        case "email":
            try:
                results = DDGS().text(query, max_results=n)
            except Exception as e:
                questionary.print(f"Search failed: {e}", "fg:red")
                return []
            return [r["href"] for r in results]
        case _:
            try:
                results = DDGS().text(query, max_results=n)
            except Exception as e:
                questionary.print(f"Search failed: {e}", "fg:red")
                return []
            return [r["href"] for r in results]
