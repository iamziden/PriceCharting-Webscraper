import utils
import scrape
import pandas as pd

# Import spreadsheet and fix columns.
df = pd.read_excel("inventory.xlsx")
utils.fix_column_types(df)

# Is the URL reachable?
url = input("Input URL: ")
if scrape.valid_url(url):
    print("Valid URL.")
else:
    print("Invalid URL.")

# Add a new row
utils.new_row(df)

# Print rows
print("\n", df[["Game", "Set", "Product", "Genre", "Quantity", "Market", "ReturnAmt", "ReturnPercent"]])

utils.update_quantity(df, url)

# Export spreadsheet.
save = input("\nWould you like to save? (Y/N): ").strip().lower()
if save == "y":
    file_name = input("Excel Filename: ").strip()
    file_name += ".xlsx"
    df.to_excel(file_name, index=False)

