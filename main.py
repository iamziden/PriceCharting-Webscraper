import pandas as pd

import menu
import utils

def main():
    df = pd.read_excel("inventory.xlsx")
    df = utils.fix_columns(df)
    utils.update_market(df)

    menu.run(df)

if __name__ == "__main__":
    main()
