# URL Shortener

A small Flask app that shortens long URLs into short codes and redirects
visitors from the short code back to the original URL.

## Running

```
python app.py
```

The server starts on `http://localhost:5000`.

## Usage

### Shorten a URL

```
curl -X POST http://localhost:5000/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://github.com/pdugar02"}'
```

### Test a redirect (paste the short_code from above)

```
curl -L http://localhost:5000/aB3xKp
```
