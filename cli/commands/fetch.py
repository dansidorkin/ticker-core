import yfinance as yf
from pathlib import Path

def run(args):
    tickers = args.tickers
    period = args.period[0]
    interval = args.interval[0]

    print(f"[fetch] Downloading: {tickers}")

    df = yf.download(tickers, period=f"{period}", interval=f"{interval}", auto_adjust=True)["Close"]

    Path("data").mkdir(exist_ok=True)
    df.to_csv("data/raw_prices.csv")

    print("[fetch] Saved to data/raw.csv")
