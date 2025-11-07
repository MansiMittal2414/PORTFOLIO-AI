import pandas as pd

# Load returns data
df = pd.read_csv("data/returns.csv", index_col=0, parse_dates=True)

features = pd.DataFrame(index=df.index)

for col in df.columns:
    stock = df[col]
    
    features[f"{col}_ret"] = stock
    features[f"{col}_roll_mean_30"] = stock.rolling(30).mean()
    features[f"{col}_roll_vol_30"] = stock.rolling(30).std()
    features[f"{col}_EMA_20"] = stock.ewm(span=20).mean()
    
    # Sharpe Ratio approx (rolling)
    features[f"{col}_sharpe_60"] = stock.rolling(60).mean() / stock.rolling(60).std()
    
    # Drawdown
    roll_max = (1 + stock).cumprod().rolling(252).max()
    curr_value = (1 + stock).cumprod()
    features[f"{col}_drawdown"] = (curr_value - roll_max) / roll_max

# Drop NaN values
features = features.dropna()

# Save features
features.to_csv("data/features.csv")
print("✅ Feature Engineering Complete — file saved at data/features.csv")
