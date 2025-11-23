import yfinance as yf
from pathlib import Path

def run(args):
    tickers = args.tickers
    print(f"[fetch] Downloading: {tickers}")

    df = yf.download(tickers, period="1mo", interval="1d", auto_adjust=True)["Close"]

    Path("data").mkdir(exist_ok=True)
    df.to_csv("data/raw.csv")

    print("[fetch] Saved to data/raw.csv")
