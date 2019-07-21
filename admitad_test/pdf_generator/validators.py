import urllib
from urllib.parse import urlparse
import re
import html5lib


def validate_url(url: str):
    if not url.startswith('http://'):
        url = f'http://${url}/'
    result = html5lib.parse(url, namespaceHTMLElements=False)

    return result is not None
