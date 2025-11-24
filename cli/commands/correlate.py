import subprocess
import numpy as np
import matplotlib.pyplot as plt

import yfinance as yf
from pathlib import Path


def run(args):
    tickers = args.tickers
    period = args.period[0]
    interval = args.interval[0]
    # DO not forget .dropna() to line-up the tickers in the time-series.
    print(f"[correlate] Downloading information for {len(tickers)} tickers...")
    df = yf.download(tickers, period=f"{period}", interval=f"{interval}", auto_adjust=True)['Close'].dropna()
    # Try-Catch Error catch here, raises  YFPricesMissingError
    print(f"[correlate] Downloaded successfully.")
    print(f"[correlate] Calculating correlation...")
    print(df.corr())

    # Do we want to save the data listed in the command-line?
    save = input("[correlate] Save correlation data? [y/n]\n")
    if save.lower() == "y":
        print(f"[correlate] Saving to data/corr.csv...")
        Path("data").mkdir(exist_ok=True)
        df.corr(method='pearson').to_csv("data/correlation.csv")
        print(f"[correlate] File saved successfully to data/correlation.csv")
        openFile = input("[correlate] Open correlation file? [y/n]\n")
        if openFile.lower() == "y":
            print(f"[correlate] Opening correlation file...")
            subprocess.run(["open", f"data/correlation.csv"], check=True)

    # Do we want a heat-map of the correlation data?
    visualization = input("[correlate] Visualize correlation data? [y/n]\n")
    if visualization.lower() == "y":
        print(f"[correlate] Visualizing correlation data...")
        correlation_matrix = np.array(df.corr())
        plt.matshow(correlation_matrix, cmap="Greens")
        plt.xticks(range(len(tickers)), tickers, rotation=90)
        plt.yticks(range(len(tickers)), tickers)

        plt.colorbar()
        plt.show()
    print("[correlate] Task completed.")



    # Will need to clean the data, as .to_csv creates a square matrix but only upper-triangular needed.
