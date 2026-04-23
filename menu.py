import utils

from datetime import datetime
from pathlib import Path

# Prints a line to seperate commands.
def print_line():
    print("\n- - - - - - - - - -")

# Recieve option input.
def get_option(prompt="Enter option: "):
    return input(prompt).strip()

# Print main menu options.
def print_main_menu():
    print_line()
    print("\n[1] Input Item")
    print("[2] Delete Item")
    print("[3] Update Item Quantity")
    print("[4] Update Item MSRP / Purchase Price")
    print("[5] Print Inventory")
    print("[9] Save As")
    print("[0] Quit")
    print_line()

# Print search menu options.
def print_search_menu():
    print_line()
    print("\n[1] Search by URL")
    print("[2] Search by Set and Product")
    print("[0] Back")
    print_line()

# Return URL for search method.
def choose_product_url(df):
    while True:
        print_search_menu()
        option = get_option()

        if option == "1":
            url = input("\nEnter PriceCharting URL: ").strip()
            if (df["URL"] == url).any():
                return url

            print("\nProduct not found.")

        elif option == "2":
            set_name = input("\nEnter Set: ").strip()
            product_type = input("Enter Product: ").strip()
            return utils.get_URL(df, set_name, product_type)

        elif option == "0":
            return None

        else:
            print("\nInvalid option.")

# Prints inventory.
def print_inventory(df):
    columns = [
        "Game",
        "Set",
        "Product",
        "Genre",
        "Quantity",
        "Market",
        "ReturnAmt",
        "ReturnPercent",
    ]
    print("\n", df[columns])

# Saves inventory.
def save_inventory(df, quit):
    if quit:
        today = datetime.today()
        formatted_date = today.strftime("%m-%d-%y")
        
        history = Path("history")
        
        file_name = "inventory"
        file_name_date = "inventory-" + formatted_date
        
        if not file_name_date.endswith(".xlsx"):
            file_name_date += ".xlsx"
            
        file_path = history / file_name_date

        df.to_excel(file_path, index=False)
        print(f"\nSaved to {file_name_date}.")
    else:
        file_name = input("Excel Filename: ").strip()
        
    if not file_name.endswith(".xlsx"):
            file_name += ".xlsx"

    df.to_excel(file_name, index=False)
    print(f"\nSaved to {file_name}.")

# Menu loop.
def run(df):
    while True:
        print_main_menu()
        option = get_option()

        if option == "1":
            utils.new_row(df)

        elif option == "2":
            print("\nDelete item is not set up yet.")

        elif option == "3":
            url = choose_product_url(df)
            if url is not None:
                utils.update_quantity(df, url)

        elif option == "4":
            url = choose_product_url(df)
            if url is not None:
                utils.update_msrp(df, url)

        elif option == "5":
            print_inventory(df)
            
        elif option == "9":
            save_inventory(df, False)

        elif option == "0":
            save_inventory(df, True)
            return

        else:
            print("\nInvalid option.")
