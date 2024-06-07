import yfinance as yf
import json

def get_Cash_Flow(symbol):
    try:
        stock = yf.Ticker(symbol)
        cash_flow = stock.cash_flow
        if not cash_flow.empty:
            # Convert DataFrame to dictionary and ensure all keys are strings
           cash_flow_dict = cash_flow.to_dict()
           cash_flow_converted = {
               str(key): {str(inner_key): inner_value for inner_key, inner_value in value.items()}
               for key, value in cash_flow_dict.items()
           }
           return cash_flow_converted
        else:
            print(f"No balance sheet data available for {symbol}")
            return None
    except Exception as e:
        print(f"Error fetching balance sheet data for {symbol}: {e}")
        return None


def save_to_file(data, filename):
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error saving data to file: {e}")

symbol = "RELIANCE.BO"
cash_flow_data = get_Cash_Flow(symbol)
if cash_flow_data is not None:
    save_to_file(cash_flow_data, f"{symbol}_cash_flow_data.json")
else:
    print(f"No data to save for {symbol}")