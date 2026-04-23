import scrape

# Fixes column types of dataframe, sets URL as index
def fix_column_types(df):
    columns = ["MSRP", "Market", "TotalMSRP", "TotalMarket", "ReturnAmt", "ReturnPercent"]
    
    for col in columns:
        df[col] = df[col].astype(float)
        
    df["Quantity"] = df["Quantity"].astype(int)
    
    return df.set_index("URL", drop=False)

# Retrieves row information from URL
def get_information(df, url):
    if not (df["URL"] == url).any():
        return None
    
    game = df.loc[df["URL"] == url, "Game"].iloc[0]
    set_name = df.loc[df["URL"] == url, "Set"].iloc[0]
    product_type = df.loc[df["URL"] == url, "Product"].iloc[0]
    quantity = df.loc[df["URL"] == url, "Quantity"].iloc[0]
    msrp = df.loc[df["URL"] == url, "MSRP"].iloc[0]
    market = df.loc[df["URL"] == url, "Market"].iloc[0]
    
    return game, set_name, product_type, quantity, msrp, market

# Retrieves URL from Set and Product
def get_URL(df, set_name, product_type):
    if not ((df["Set"] == set_name) & (df["Product"] == product_type)).any():
        print("\nProduct not found.")
        return None
    
    url = df.loc[
        (df["Set"] == set_name) & (df["Product"] == product_type),
        "URL"].iloc[0]
    
    return url

# Retrieve Product from URL
def get_product(df, url):
    product_type = df.loc[df["URL"] == url, "Product"].iloc[0]
    if product_type:
        return product_type
    else:
        return None

# Retrieve Set from URL
def get_set(df, url):
    set_name = df.loc[df["URL"] == url, "Set"].iloc[0]
    if set_name:
        return set_name
    else:
        return None
    
# Calculate TotalMSRP, TotalMarket, ReturnAmt, ReturnPercent
def calculate_totals(quantity, msrp, market):
    if msrp == 0: return None
    
    total_msrp = int(quantity) * float(msrp)
    total_market = int(quantity) * float(market)
    return_amount = total_market - total_msrp
    return_percent = float(round(total_market / total_msrp * 100, 2))
    
    return total_msrp, total_market, return_amount, return_percent

# Update TotalMSRP, TotalMarket, ReturnAmt, ReturnPercent
def update_totals(df, url=None):
    if url is not None:
        if not (df["URL"] == url).any():
            print("Product not found.")
            return None

        rows = df["URL"] == url
    else:
        rows = df.index

    for index in df.loc[rows].index:
        quantity = df.loc[index, "Quantity"]
        msrp = df.loc[index, "MSRP"]
        market = df.loc[index, "Market"]

        total_msrp, total_market, return_amount, return_percent = calculate_totals(
            quantity,
            msrp,
            market
        )

        df.loc[index, "TotalMSRP"] = total_msrp
        df.loc[index, "TotalMarket"] = total_market
        df.loc[index, "ReturnAmt"] = return_amount
        df.loc[index, "ReturnPercent"] = return_percent

    print("Totals updated.")

# Adds a new row
def new_row(df, url):
    if scrape.valid_url(url) == False:
        print("\nInvalid URL. No changes were made.")
        return None
    if (df["URL"] == url).any():
        print("\nURL already exists. No changes were made.")
        return None
    
    quantity = input("Enter product quantity: ")
    try:
        val = int(quantity)
    except ValueError:
        print("\nInvalid Quantity. Product will not be saved.")
        return None
    
    msrp = input("Enter MSRP (Retail): ")
    try:
        val = float(msrp)
    except ValueError:
        print("\nInvalid MSRP. Product will not be saved.")
        return None
    
    game_name, set_name, product_type, market, genre = scrape.product_details(url)
    
    total_msrp, total_market, return_amount, return_percent = calculate_totals(quantity, msrp, market)
    
    df.loc[url] = {
        "URL": url,
        "Game": game_name,
        "Set": set_name,
        "Product": product_type,
        "Genre": genre,
        "Quantity": quantity,
        "MSRP": msrp,
        "Market": market,
        "TotalMSRP": total_msrp,
        "TotalMarket": total_market,
        "ReturnAmt": return_amount,
        "ReturnPercent": return_percent
    }
    
    print("\n", game_name, ":", set_name, product_type, "has been inputted.")
    
# Delete row
def delete_row(df, url):
    if not (df["URL"] == url).any():
        print("\nProduct not found.")
        return None
    
    game_name, set_name, product_type, _, _, _ = get_information(df, url)
    
    option = input(f"\n{game_name}: {set_name} {product_type} will be removed. Proceed? (Y/N): ").strip().lower()
    if option == ("y"):
        df.drop(index=url, inplace=True)
        print("\n", game_name, ":", set_name, product_type, "has been removed.")
    else:
        print("\nNo changes were made.")
    
# Update quantity of given product
def update_quantity(df, url):
    if not (df["URL"] == url).any():
        print("\nProduct not found.")
        return None
    
    game_name, set_name, product_type, quantity, msrp, market = get_information(df, url)
    
    print("\nThe current quantity of", set_name, product_type, "is", quantity, ".")
    new_quantity = input("Enter new quantity: ").strip()
    
    try:
        new_quantity = int(new_quantity)
    except ValueError:
        print("\nInvalid quantity. No changes were made.")
        return None
    if new_quantity == quantity:
        print("\nQuantity is already", quantity, ". No changes were made.")
        return None
    elif new_quantity <= 0:
        print("\nQuantity cannot less than or equal to 0. No changes were made.")
        return None
    
    total_msrp, total_market, return_amount, return_percent = calculate_totals(
        new_quantity, msrp, market
    )
    
    df.loc[df["URL"] == url, "Quantity"] = new_quantity
    df.loc[df["URL"] == url, "TotalMSRP"] = total_msrp
    df.loc[df["URL"] == url, "TotalMarket"] = total_market
    df.loc[df["URL"] == url, "ReturnAmt"] = return_amount
    df.loc[df["URL"] == url, "ReturnPercent"] = return_percent
    
    print("\n", "Quantity of", game_name, ":", set_name, product_type, "has been changed to", new_quantity)

# Update MSRP / Cost of given product.
def update_msrp(df, url):
    if not (df["URL"] == url).any():
        print("\nProduct not found.")
        return None
    
    game_name, set_name, product_type, quantity, msrp, market = get_information(df, url)
    
    print("\nThe current MSRP / Cost of", set_name, product_type, "is", msrp, ".")
    new_msrp = input("Enter new MSRP / Cost: ").strip()
    
    try:
        new_msrp = float(new_msrp)
    except ValueError:
        print("\nInvalid MSRP / Cost. No changes were made.")
        return None
    if new_msrp == msrp:
        print("\nMSRP / Cost is already", msrp, ". No changes were made.")
        return None
    elif new_msrp <= 0:
        print("\nMSRP / Cost cannot be less than or equal to 0. No changes were made.")
        return None
    
    total_msrp, total_market, return_amount, return_percent = calculate_totals(
        quantity, new_msrp, market
    )
    
    df.loc[df["URL"] == url, "MSRP"] = new_msrp
    df.loc[df["URL"] == url, "TotalMSRP"] = total_msrp
    df.loc[df["URL"] == url, "ReturnAmt"] = return_amount
    df.loc[df["URL"] == url, "ReturnPercent"] = return_percent
    
    print("\n", "MSRP / Cost of", game_name, ":", set_name, product_type, "has been changed to", new_msrp)
    