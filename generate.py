import email.utils

from datetime import datetime, UTC
from xml.etree import ElementTree

import requests

ECOSPHERES_URL = "https://ecologie.data.gouv.fr"
DATAGOUVFR_URL = "https://www.data.gouv.fr/api"
UNIVERSE_NAME = "univers-ecospheres"

STATIC_URLS = [
    "/",
    "/bouquets",
    "/about",
]


def parse_http_date_with_tz(http_date_str):
    dt = email.utils.parsedate_to_datetime(http_date_str)
    return dt.replace(tzinfo=UTC)


def fetch_urls():
    results = []

    for url in STATIC_URLS:
        page_url = f"{ECOSPHERES_URL}{url}"
        r = requests.get(page_url)
        r.raise_for_status()
        results.append({
            "url": page_url,
            "last_modified": parse_http_date_with_tz(
                r.headers['last-modified']
            ),
        })

    r = requests.get(f"{DATAGOUVFR_URL}/2/topics", params={
        "tag": UNIVERSE_NAME,
    })
    r.raise_for_status()
    data = r.json()
    assert data["next_page"] is None

    for bouquet in data["data"]:
        results.append({
            "url": f"{ECOSPHERES_URL}/bouquets/{bouquet['slug']}",
            "last_modified": datetime.fromisoformat(bouquet["last_modified"]),
        })

    return results


def create_sitemap(urls):
    """Creates a sitemap XML from a list of URLs."""
    sitemap = ElementTree.Element("urlset", {
        "xmlns": "http://www.sitemaps.org/schemas/sitemap/0.9"
    })

    for url_data in urls:
        url_element = ElementTree.SubElement(sitemap, "url")
        loc = ElementTree.SubElement(url_element, "loc")
        loc.text = url_data["url"]
        lastmod = ElementTree.SubElement(url_element, "lastmod")
        lastmod.text = url_data["last_modified"].isoformat()

    tree = ElementTree.ElementTree(sitemap)
    ElementTree.indent(tree)
    tree.write("sitemap.xml")


if __name__ == "__main__":
    urls = fetch_urls()
    create_sitemap(urls)
