from playwright.sync_api import sync_playwright


def pull(url):
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        pg.goto(url, wait_until="load")
        pg.wait_for_timeout(2000)
        html = pg.content()
        b.close()
    return html
