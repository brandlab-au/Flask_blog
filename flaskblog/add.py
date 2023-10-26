from yfinance import Ticker

# Function to get closing price for a stock
def get_closing_price(stock_symbol):
    try:
        stock_data = Ticker(stock_symbol)
        stock_info = stock_data.history(period="1d")
        closing_price = stock_info['Close'][0]
        return closing_price
    except Exception as e:
        return str(e)

# Get user input for stock symbol
# stock_symbol = input("Enter the stock symbol (e.g., AAPL): ")


def process_input(user_input):
    print(f"Received user input: {user_input}")

stock_symbol = "AAPL"
# Get and display the closing price
closing_price = get_closing_price(stock_symbol)

# if isinstance(closing_price, float):
#     return closing_price
# else:
#     return(f"The closing price of {stock_symbol} today is: ${closing_price:.2f}")





