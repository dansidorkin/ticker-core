"""
Created by Daniel Mishan Sat Nov 22 in Oakhurst, CA
Project Name: Ticker-Core

This project uses yfinance and visualizes correlations by price movements in market. For example,
suppose that $NVDA and $MSFT both move downwards during a specific period (1d, 1wk, 1mo, 1yr, ytd).
Then, they are both correlated. We use the Pearson Correlation to determine correlation trends.
We plot X-axis as the date, and plot Y-axis as the
"""
import pandas as pd #For Data
import yfinance as yf
# import seaborn as sns # (for data visualization)
import matplotlib.pyplot as plt
import networkx as nx


def main():
    print("This program visualizes market movements.")
    df = yf.download(["MU", "AAPL", "AMZN",
                      "EQT","BTC-USD",
                      "TSM", "NVDA", "AMD", "MSFT",
                      "ASML", "MP"], period="1mo", interval="1d")["Close"].dropna() # drop NaN values
    df = df.rename(columns={"GC=F": "GOLD"})
    # sns.regplot(x="GOLD", y="NVDA", data=df)

    # 1. Correlation matrix
    corr = df.corr()
    print(corr)
    # 2. Create graph
    G = nx.Graph()

    # 3. Add weighted edges (no duplicates)
    for i in range(len(corr.columns)):
        for j in range(i + 1, len(corr.columns)):
            stock1 = corr.columns[i]
            stock2 = corr.columns[j]
            weight = corr.iloc[i, j]
            G.add_edge(stock1, stock2, weight=weight)

    edge_colors = [
        "red" if G[u][v]['weight'] < 0 else "blue"
        for u, v in G.edges()
    ]

    plt.figure(figsize=(16, 16))

    # 4. Draw graph (edge thickness = correlation strength)
    pos = nx.spring_layout(G, k=20, iterations=400, scale=5, seed=42)
    weights = [abs(G[u][v]['weight']) * 5 for u, v in G.edges()]

    nx.draw(G, pos,
            with_labels=True,
            node_size=2000,
            width=weights,
            node_color="skyblue",
            edge_color=edge_colors)

    # 6. Draw edge labels (rounded to 2 decimals)
    labels = {(u, v): f"{corr.loc[u, v]:.2f}" for u, v in G.edges()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=16)

    plt.show()

if __name__ == '__main__':
    main()