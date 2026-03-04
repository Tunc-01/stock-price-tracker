import yfinance as yf
import matplotlib.pyplot as plt

def main():
    print("Stock Price Tracker")
    symbol = input("Enter stock symbol (e.g., AAPL, MSFT, TSLA): ").strip().upper()

    try:
        data = yf.download(symbol, period="1mo", interval="1d", progress=False)
        if data.empty:
            print("No data found. Check the symbol and try again.")
            return

        plt.figure()
        data["Close"].plot(title=f"{symbol} - Close Price (Last 1 Month)")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.show()

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
