import scrape

# Return product from URL.
def get_product(df, url):
    product = df.loc[df["URL"] == url, "Product"].iloc[0]
    if product:
        return product
    else:
        return None

# Return market price of specified product.
def get_market(df, product):
    market = df.loc[df["Product"] == product, "Market"].iloc[0]
    if market:
        return market
    else:
        return None
    
# Return MSRP (Retail) price of specified product.
def get_msrp(df, product):
    msrp = df.loc[df["Product"] == product, "MSRP"].iloc[0]
    if msrp:
        return msrp
    else:
        return None

# Return Quantity of specified product.
def get_quantity(df, product):
    quantity = df.loc[df["Product"] == product, "Quantity"].iloc[0]
    if quantity:
        return quantity
    else:
        return None

# Return total market price of specified product.
def get_total_market(df, product):
    totalMarket = df.loc[df["Product"] == product, "TotalMarket"].iloc[0]
    if totalMarket:
        return totalMarket
    else:
        return None
    
# Return total MSRP (Retail) price of specified product.
def get_total_msrp(df, product):
    totalMsrp = df.loc[df["Product"] == product, "TotalMSRP"].iloc[0]
    if totalMsrp:
        return totalMsrp
    else:
        return None

# Return Return% of specified product.
def get_return(df, product):
    returnamount = df.loc[df["Product"] == product, "Return"].iloc[0]
    if returnamount:
        return returnamount
    else:
        return None
    
# Return Return% of specified product.
def get_return_percent(df, product):
    returnpercent = df.loc[df["Product"] == product, "ReturnPercent"].iloc[0]
    if returnpercent:
        return returnpercent
    else:
        return None

# Adds a new row
def new_row(df):
    url = input("Enter PriceCharting URL: ")
    if scrape.valid_url(url) == False:
        print("Invalid URL. Product will not be saved.")
        return None
    
    quantity = input("Enter product quantity: ")
    try:
        val = int(quantity)
    except ValueError:
        print("Invalid Quantity. Product will not be saved.")
        return None
    
    msrp = input("Enter MSRP (Retail): ")
    try:
        val = float(msrp)
    except ValueError:
        print("Invalid MSRP. Product will not be saved.")
        return None
    
    game_name, set_name, product_type, market, genre = scrape.product_details(url)
    
    totalmsrp = float(msrp) * int(quantity)
    totalmarket = float(market) * int(quantity)
    returnamount = totalmarket - totalmsrp
    returnpercent = round(totalmarket / totalmsrp * 100)
    
    df.loc[len(df)] = {
        "URL": url,
        "Game": game_name,
        "Set": set_name,
        "Product": product_type,
        "Genre": genre,
        "Quantity": quantity,
        "MSRP": msrp,
        "Market": market,
        "TotalMSRP": totalmsrp,
        "TotalMarket": totalmarket,
        "Return": returnamount,
        "ReturnPercent": returnpercent
    }
