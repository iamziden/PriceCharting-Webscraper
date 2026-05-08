# PriceCharting Web Scraper & Inventory Tracker

A Python project for tracking inventory and current market prices with PriceCharting.com.

## Features

- Loads inventory from an Excel spreadsheet
- Updates market prices
- Add new items
- Delete existing items
- Update quantity
- Update cost
- Search inventory by features
- Saves changes to the inventory file
- Creates history files for tracking inventory over time

## Installation

1. Clone the repository:
```sh
git clone https://github.com/iamziden/PriceCharting-Webscraper
```

2. Move into the project folder:
```sh
cd PriceCharting-Webscraper
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

## How to Run

Run the program with:
```sh
python main.py
```

## Example Usage

Example workflow:

1. Start the program
```sh
python main.py
```

2. Choose an operation
```sh
[1] Input Item
```

3. Enter required fields
```sh
Enter PriceCharting URL: https://www.pricecharting.com/game/pokemon-prismatic-evolutions/booster-bundle
Enter Quantity: 1
Enter Cost: 30
```

The program then scrapes the product details (such as name and price), adds the item to the inventory, calculates metrics, and updates the spreadsheet.

## Inventory Analytics
Because the program stores inventory data in pandas DataFrames and Excel files, it can be expanded for more detailed analytics. For example, the history files can be used to track total inventory value over time, day/month/year changes, returns, and individual product preformance.

## Usage

The program provides the following operations:
- `Input Item` - Adds an item using a PriceCharting URL
- `Delete Item` - Removes an item using either by URL or by Set and Product
- `Update Item Quantity` - Updates an item's quantity either by URL or by Set and Product
- `Update Item Cost` - Updates an item's cost either by URL or by Set and Product
- `Print Inventory` - Prints the entire inventory along with several fields
- `Search Inventory` - Prints part of the inventory, searched by URL, Set, or Product

## Future Improvements

- Improved search methods
- Improved summary statistics (%Change over time, etc.)
- Operations for more detailed inventory analytics
- Discord bot integration for daily inventory reports
