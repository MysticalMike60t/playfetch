from html.parser import HTMLParser

# I need to look at this more:
# https://docs.python.org/3/library/html.parser.html


class HTML(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)


def html(html):  # Add type defs
    parser = HTML()
    parser.feed(html)
    # soup = BS(raw_html, "lxml")
    # return soup
