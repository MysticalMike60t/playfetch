import gzip
import zlib

from config import CONFIG

# def html(raw_bytes):
#     charset = raw_bytes.headers.get_content_charset() or "utf-8"
#     html = raw_bytes.read().decode(charset, errors="replace")
#     return html


def http_res_content_compression(res) -> str:  # Add type defs
    data = res.read()  # Add type defs
    encoding = (res.headers.get("Content-Encoding") or "").lower()  # Add type defs

    if encoding == "gzip":
        data = gzip.decompress(data)  # Add type defs
    elif encoding == "deflate":
        try:
            data = zlib.decompress(data)  # Add type defs
        except zlib.error:
            data = zlib.decompress(data, -zlib.MAX_WBITS)  # Add type defs
    elif encoding == "br":
        import brotli

        data = brotli.decompress(data)

    charset = (
        res.headers.get_content_charset() or CONFIG.defaults.http_res_content_encoding
    )  # Add type defs
    return data.decode(charset, errors="replace")
