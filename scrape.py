import requests
import pandas as pd
from bs4 import BeautifulSoup

# Scrape market price from specified URL.
def scrape_market_price(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    price_tag = soup.select_one("td#used_price span.price.js-price")
    
    if price_tag:
        price = price_tag.get_text(strip=True).replace("$", "")
        return price
    else:
        return None
    
def get_product(url):
    product = df.loc[df["URL"] == url, "Product"].iloc[0]
    if product:
        return product
    else:
        return None

# Return market price of specified product.
def get_market(product):
    market = df.loc[df["Product"] == product, "Market"].iloc[0]
    if market:
        return market
    else:
        return None
    
# Return MSRP (Retail) price of specified product.
def get_msrp(product):
    msrp = df.loc[df["Product"] == product, "MSRP"].iloc[0]
    if msrp:
        return msrp
    else:
        return None

# Return Quantity of specified product.
def get_quantity(product):
    quantity = df.loc[df["Product"] == product, "Quantity"].iloc[0]
    if quantity:
        return quantity
    else:
        return None

# Return total market price of specified product.
def get_total_market(product):
    totalMarket = df.loc[df["Product"] == product, "TotalMarket"].iloc[0]
    if totalMarket:
        return totalMarket
    else:
        return None
    
# Return total MSRP (Retail) price of specified product.
def get_total_msrp(product):
    totalMsrp = df.loc[df["Product"] == product, "TotalMSRP"].iloc[0]
    if totalMsrp:
        return totalMsrp
    else:
        return None

# Return Return% of specified product.
def get_return(product):
    percent = df.loc[df["Product"] == product, "Return"].iloc[0]
    if percent:
        return percent
    else:
        return None
        
# - - - - -

# Import from spreadsheet.
df = pd.read_excel("inventory.xlsx")
    
df["Market"] = df["URL"].apply(scrape_market_price)
    
df["Market"] = pd.to_numeric(df["Market"], errors="coerce").fillna(0).astype(float)
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce").fillna(0).astype(int)

df["Return"] = round((df["Market"] / df["MSRP"] * 100), 2)
df["TotalMSRP"] = df["MSRP"] * df["Quantity"]
df["TotalMarket"] = df["Market"] * df["Quantity"]
df["Profit"] = df["TotalMarket"] - df["TotalMSRP"]

Portfolio = df["TotalMarket"].sum()
Retail = df["TotalMSRP"].sum()
Profit = Portfolio - Retail
Return = round((Portfolio / Retail * 100), 2)

print("Portfolio:", Portfolio)
print("Retail:", Retail)
print("Profit:", Profit)
print("Return:", Return, "%")

# Save updated spreadsheet.
df.to_excel('new_inventory.xlsx', index=False)

print("MSRP of 151 Booster Bundle:", get_msrp('151 Booster Bundle'))
print("Market of 151 Booster Bundle:", get_market('151 Booster Bundle'))

print(get_total_market('Prismatic Booster Bundle'))
