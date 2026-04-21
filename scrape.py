import requests

from bs4 import BeautifulSoup

# Return scraped product details from URL.
# Input: URL
# Output: Set, Product, Market, Genre
def product_details(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    name = soup.select_one("h1#product_name").get_text(strip=True)
    product_type, set_name = name.split("Pokemon ", 1)
    
    genre = soup.select_one('td.details[itemprop="genre"]').get_text(strip=True)
    
    price = soup.select_one("td#used_price span.price.js-price")
    price = price.get_text(strip=True).replace("$", "").replace(",", "")
    price = float(price)
    
    return set_name, product_type, price, genre

# Return if URL can be reached.
def valid_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
        }
    
    try:
        response = requests.get(url, headers=headers)
        return response.status_code == 200
    except requests.RequestException:
        return False
