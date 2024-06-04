from datetime import datetime, UTC

from flask import Flask, make_response
from flask_caching import Cache

from generate import generate

app = Flask(__name__)

app.config["CACHE_TYPE"] = "FileSystemCache"
app.config["CACHE_DIR"] = "/tmp"
cache = Cache(app)


@app.route("/sitemap.xml")
@cache.cached(timeout=3600 * 3)
def sitemap():
    response = make_response(generate(write=False))
    response.headers["Content-Type"] = "application/xml; charset=utf-8"
    last_modified = datetime.now(UTC).strftime('%a, %d %b %Y %H:%M:%S GMT')
    response.headers["Last-Modified"] = last_modified
    return response
