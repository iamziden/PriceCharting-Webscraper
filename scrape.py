import utils
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Import from spreadsheet.
df = pd.read_excel("inventory.xlsx")

# Scrape market prices from PriceCharting
df["Market"] = df["URL"].apply(utils.scrape_market_price)

# Change column types
df["Market"] = pd.to_numeric(df["Market"], errors="coerce").fillna(0).astype(float)
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce").fillna(0).astype(int)

# Calculate
df["ReturnPercent"] = round((df["Market"] / df["MSRP"] * 100), 2)
df["TotalMSRP"] = df["MSRP"] * df["Quantity"]
df["TotalMarket"] = df["Market"] * df["Quantity"]
df["Return"] = df["TotalMarket"] - df["TotalMSRP"]

Portfolio = df["TotalMarket"].sum()
Retail = df["TotalMSRP"].sum()
ReturnAmount = Portfolio - Retail
ReturnPercent = round((Portfolio / Retail * 100), 2)

print("Portfolio:", Portfolio)
print("Retail:", Retail)
print("Profit:", ReturnAmount)
print("Return:", ReturnPercent, "%")

print("MSRP of 151 Booster Bundle:", utils.get_msrp(df, '151 Booster Bundle'))
print("Market of 151 Booster Bundle:", utils.get_market(df, '151 Booster Bundle'))

print(utils.get_total_market(df, 'Prismatic Booster Bundle'))

print(df.head())

# Save updated spreadsheet.
df.to_excel('new_inventory.xlsx', index=False)