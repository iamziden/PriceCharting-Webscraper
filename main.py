import utils
import scrape
import pandas as pd

# Import spreadsheet.
df = pd.read_excel("inventory.xlsx")

# Is the URL reachable?
url = input("Input URL: ")
if scrape.valid_url(url) == False:
    print("Invalid URL.")
else:
    print("Valid URL.")

# Add a new row
utils.new_row(df)

# Print rows
print(df[["Game", "Set", "Product", "Genre", "Quantity", "Market", "Return", "ReturnPercent"]])

# Export spreadsheet.
if input("Would you like to save? (Y/N): ") == ("Y" or "y"):
    file_name = input("Excel Filename: ").strip()
    file_name += ".xlsx"
    df.to_excel(file_name, index=False)
