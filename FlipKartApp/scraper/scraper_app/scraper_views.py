import requests
from bs4 import BeautifulSoup

def scrape_product(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find("span", {"class": "_35KyD6"})
    if title:
        title = title.get_text()
    else:
        title = "Title not found"

    description = soup.find("div", {"class": "_3LWZlK"})
    if description:
        description = description.get_text()
    else:
        description = "Description not found"

    price = soup.find("div", {"class": "_30jeq3 _1_WHN1"})
    if price:
        price = price.get_text()
    else:
        price = "Price not found"
        
    # Add additional code to extract other required data
    return title, description, price
