import pandas as pd
import yfinance as yf
from datetime import datetime
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import accuracy_score

# -----------------------
# TXT Output
# -----------------------
def write_output_txt(filename, results):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("===================================\n")
        f.write("   ENERGY FORECAST – CODE A\n")
        f.write("===================================\n")
        f.write(f"Run time (UTC): {datetime.utcnow():%Y-%m-%d %H:%M:%S UTC}\n\n")
        for asset in results:
            f.write(f"--------- {asset['name']} ---------\n")
            f.write(f"Data date : {asset['date']}\n")
            if 'cv_mean' in asset:
                f.write(f"Model CV  : {asset['cv_mean']:.2%} ± {asset['cv_std']:.2%}\n")
            f.write(f"Prob UP   : {asset['prob_up']:.2%}\n")
            f.write(f"Prob DOWN : {asset['prob_down']:.2%}\n")
            f.write(f"Signal    : {asset['signal']}\n\n")
        f.write("===================================\n")

# -----------------------
# Feature Builders
# -----------------------
def build_trend_vol_features(df, price_col="Close", trend_windows=[5, 20], vol_window=10):
    df = df.copy()
    df["ret"] = df[price_col].pct_change()
    for w in trend_windows:
        df[f"trend_{w}"] = df[price_col].pct_change(w)
    df[f"vol_{vol_window}"] = df["ret"].rolling(vol_window).std()
    df.dropna(inplace=True)
    return df

def build_zscore(df, col, window=60):
    df = df.copy()
    mean = df[col].rolling(window).mean()
    std = df[col].rolling(window).std()
    df[f"{col}_z"] = (df[col] - mean) / std
    return df
