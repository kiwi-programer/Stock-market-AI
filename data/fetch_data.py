import yfinance as yf
import pandas as pd
from typing import List

def fetch_historical_data(ticker: str, start: str, end: str) -> pd.DataFrame:
    """
    Download historical stock price data using yfinance.
    """
    df = yf.download(ticker, start=start, end=end)
    df.reset_index(inplace=True)
    df["ticker"] = ticker
    return df

def fetch_batch_data(tickers: List[str], start: str, end: str) -> pd.DataFrame:
    """
    Download data for multiple tickers and combine into one DataFrame.
    """
    all_data = []
    for ticker in tickers:
        print(f"Fetching data for {ticker}")
        df = fetch_historical_data(ticker, start, end)
        all_data.append(df)
    return pd.concat(all_data)
