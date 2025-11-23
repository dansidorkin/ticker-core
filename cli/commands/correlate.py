import yfinance as yf
from pathlib import Path


def run(args):
    tickers = args.tickers
    # DO not forget .dropna() to line-up the tickers in the time-series.
    print(f"[correlate] Downloading information for {len(tickers)} tickers...")
    df = yf.download(tickers, period="1mo", interval="1d", auto_adjust=True)['Close'].dropna()
    # Try-Catch Error catch here, raises  YFPricesMissingError
    print(f"[correlate] Downloaded successfully.")
    print(f"[correlate] Calculating correlation...")
    Path("data").mkdir(exist_ok=True)

    df.corr(method='pearson').to_csv("data/correlation_raw.csv")
    print(f"[correlate] Saving to data/correlation_raw.csv...")
    print(f"[correlate] Done")

    # Will need to clean the data, as .to_csv creates a square matrix but only upper-triangular needed.
