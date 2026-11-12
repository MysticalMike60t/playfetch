import re

EMAIL_RE = re.compile(
    r"(?<![\w.!#$%&'*+/=?^`{|}~-])"
    r"(?=[^@\s]{1,64}@)"
    r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*"
    r"@"
    r"(?=[a-z0-9.-]{4,253}(?![a-z0-9.-]))"
    r"(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+"
    r"(?!(?:png|jpe?g|gif|svg|webp|avif|bmp|ico|tiff?|css|js|mjs|json|xml|html?"
    r"|php|aspx?|txt|pdf|zip|gz|mp[34]|mov|woff2?|ttf)(?![a-z0-9-]))"
    r"(?:[a-z]{2,63}|xn--[a-z0-9-]{1,59})"
    r"(?![\w-]|\.[a-z0-9])",
    re.IGNORECASE,
)

IPV4_ADDR_RE = re.compile(r"^(?:0|10)\.\d{1,3}\.\d{1,3}\.\d{1,3}")

SUBDOMAIN_WWW_RE = re.compile(r"(.*?)\:(.*)")
