from yfinance import Ticker

# Function to get closing price for a stock
def process_input(user_input):
        stock_data = Ticker(user_input)
        stock_info = stock_data.history(period="1d")
        result1 = round(stock_info['Close'][0],2)
        result2= round(stock_info['Open'][0],2)
        return result1, result2

