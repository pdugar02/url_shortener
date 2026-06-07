import random
import string
from db import get_db
from models import create_link, get_link
from datetime import datetime as dt
from urllib.parse import urlparse
import ipaddress

ALPHABET = string.ascii_letters + string.digits
MAX_RETRIES=3
LOCAL_HOSTS=["localhost", "127.0.0.1", "::1"]


def generate_code() -> str:
    return "".join(random.choices(ALPHABET, k=6))

def shorten(long_url: str, expires_at = None):
    code = generate_code()
    row = get_link(code)
    retries=1
    while row and retries<MAX_RETRIES:
        retries+=1
        code = generate_code()
        row = get_link(code)
    if retries==MAX_RETRIES:
        raise RuntimeError("Failed to generate a short code after max retries")
    new_row = create_link(code, long_url, expires_at)
    return {"short_code": code, "short_url": f"sho.rt/{code}", "expires_at": expires_at}

def resolve(code):
    row = get_link(code)
    if row is None:
        return None
    return row["long_url"]

def validate_url(url):
    if url[:7]!="http://" and url[:8]!="https://":
        raise ValueError("The url must start with http:// or https://")
    host = urlparse(url).hostname
    if host in LOCAL_HOSTS:
        raise ValueError("The url has a local host.")
    try:
        if ipaddress.ip_address(host).is_private():
            raise ValueError("The url has a private host.")
    except ValueError as e:
        if "private host" in str(e):
            raise
        pass

    