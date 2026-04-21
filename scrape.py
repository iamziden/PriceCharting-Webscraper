import requests

from bs4 import BeautifulSoup

# Return scraped product details from URL.
# Input: URL
# Output: Game, Set, Product, Market, Genre
def product_details(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Most popular Trading Card Games
    tgc = ["Pokemon", "Digimon", "Dragon Ball", "Lorcana", "Magic", "Marvel", "One Piece", "Star Wars", "YuGiOh"]
    
    name = soup.select_one("h1#product_name").get_text(strip=True)
    product_type = ""
    set_name = ""
    game_name = ""
    
    for game in tgc:
        if game in name:
            left, right = name.split(game, 1)
            product_type = left.strip()
            set_name = right.strip()
            game_name = game
            break
    
    genre = soup.select_one('td.details[itemprop="genre"]').get_text(strip=True)
    
    price = soup.select_one("td#used_price span.price.js-price")
    price = price.get_text(strip=True).replace("$", "").replace(",", "")
    price = float(price)
    
    return game_name, set_name, product_type, price, genre,

# Return if URL can be reached.
def valid_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
        }
    
    price_charting = "https://www.pricecharting.com/game/"
    
    try:
        if price_charting not in url:
            return False
        response = requests.get(url, headers=headers)
        return response.status_code == 200
    except requests.RequestException:
        return False
