import pytest
from shortener import shorten, validate_url, resolve
from datetime import datetime, timezone, timedelta
from db import init_db

init_db()

VALID_URL = 'https://github.com/pdugar02'
INVALID_URL = 'http://localhost:3000/'

def validate_length():
    result = shorten(VALID_URL)
    assert len(result['short_code'])==6
    
def handle_expired():
    past = datetime.now(timezone.utc) - timedelta(days=1)
    result = shorten(VALID_URL, expires_at=past.isoformat())
    assert resolve(result['short_code']) is None

def catch_invalid():
    with pytest.raises(ValueError):
        validate_url(INVALID_URL)
