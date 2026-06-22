import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

def get_books():
    books = []

    for page in range(1, 51):  # Pages 1 to 50
        url = BASE_URL.format(page)
        response = requests.get(url)

        if response.status_code != 200:
            continue

        soup = BeautifulSoup(response.text, "lxml")

        for book in soup.find_all("article", class_="product_pod"):
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            availability = book.find("p", class_="instock availability").text.strip()
            rating = book.p["class"][1]

            books.append({
                "Title": title,
                "Price": price,
                "Availability": availability,
                "Rating": rating
            })

    return books