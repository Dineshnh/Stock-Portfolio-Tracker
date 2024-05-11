import requests

# Function to fetch real-time stock data from Alpha Vantage API
def get_stock_data(symbol, api_key): 	url=f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

#Add a new stock 
def add_stock(portfolio, symbol, api_key):
    stock_data = get_stock_data(symbol, api_key)
    if "Global Quote" in stock_data:
        portfolio[symbol] = stock_data["Global Quote"]
        print(f"{symbol} added to the portfolio.")
    else:
        print(f"Failed to add {symbol}. Please check the symbol.")

#Remove a stock 
def remove_stock(portfolio, symbol):
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"{symbol} removed from the portfolio.")
    else:
        print(f"{symbol} not found in the portfolio.")

# Display the portfolio 
def display_portfolio(portfolio):
    print("\nPortfolio Overview:")
    for symbol, data in portfolio.items():
        print(f"{symbol}:")
        print(f"  Price: {data['05. price']}")
        print(f"  Change: {data['10. change percent']}")
        print()

def main():
    api_key = "YOUR_ALPHA_VANTAGE_API_KEY"
    portfolio = {}

    while True:
        print("\nOptions:")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Display Portfolio")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            symbol = input("Enter the stock symbol: ").upper()
            add_stock(portfolio, symbol, api_key)
        elif choice == "2":
            symbol = input("Enter the stock symbol to remove: ").upper()
            remove_stock(portfolio, symbol)
        elif choice == "3":
            display_portfolio(portfolio)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()