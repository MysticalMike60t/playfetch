from playwright.sync_api import sync_playwright

from config import DEFAULT_USER_AGENT


def pull(url):
    with sync_playwright() as p:
        b = p.firefox.launch(  # firefox since chromium jsut refused to work
            headless=True
        )
        c = b.new_context(
            user_agent=DEFAULT_USER_AGENT,
            ignore_https_errors=True,
        )  # deafault user_agent was triggering anri scrape
        pg = c.new_page()

        try:
            pg.goto(
                url, timeout=10000, wait_until="domcontentloaded"
            )  # waits for document load, stops after 10s, uses "domcontentloaded" instead of "load" to avoid more advanced sites from inf loading
            html = pg.content()
            return html
        except Exception as e:
            raise RuntimeError(f"Failed to load {url}: {e}")
        finally:  # close context and browser, no if and or buts
            c.close()
            b.close()
