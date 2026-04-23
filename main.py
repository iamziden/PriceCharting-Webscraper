import pandas as pd

import menu
import utils

def main():
    df = pd.read_excel("inventory.xlsx")
    utils.fix_column_types(df)

    menu.run(df)

if __name__ == "__main__":
    main()
