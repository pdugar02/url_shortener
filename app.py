from flask import Flask, redirect, jsonify, request, abort
from db import init_db
from shortener import shorten, resolve, validate_url

app = Flask(__name__)
init_db()

@app.post("/shorten")
def shorten_url():
    body = request.get_json()
    url = body.get("url")
    expires_at = body.get("expires_at")  # optional ISO string
    if not url:
        return jsonify({"error": "url is required"}), 400
    try:
        validate_url(url)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    result = shorten(url, expires_at=expires_at)
    return jsonify(result), 201

@app.get("/<code>")
def redirect_url(code):
    long_url = resolve(code)
    if long_url is None:
        abort(410)
    return redirect(long_url, code=302)

if __name__ == "__main__":
    app.run(debug=True)