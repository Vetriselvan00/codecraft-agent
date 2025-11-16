"""
Tools used by CodeCraft Agent.
"""

from typing import List, Dict, Any
import requests
from bs4 import BeautifulSoup


def fetch_products_from_category(category_url: str) -> Dict[str, Any]:
    """
    Scrapes products from the demo ecommerce page.
    """
    resp = requests.get(category_url, timeout=15)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    thumbnails = soup.select(".thumbnail")

    products: List[Dict[str, Any]] = []

    for item in thumbnails:
        name_tag = item.select_one(".title")
        price_tag = item.select_one(".price")
        rating_tags = item.select(".glyphicon-star")
        desc_tag = item.select_one(".description")

        if not name_tag or not price_tag:
            continue

        name = name_tag.get("title", name_tag.text.strip())
        raw_price = price_tag.text.strip().replace("$", "")

        try:
            price = float(raw_price)
        except ValueError:
            price = 0.0

        rating = float(len(rating_tags))
        description = desc_tag.text.strip() if desc_tag else ""
        url = "https://webscraper.io" + name_tag.get("href", "")

        products.append({
            "name": name,
            "price": price,
            "rating": rating,
            "description": description,
            "url": url,
        })

    return {"products": products}


def save_recommendation_report_to_file(report: str, filename: str):
    """
    Save the final report to a Markdown file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report)

    return {"status": "success", "filename": filename}
