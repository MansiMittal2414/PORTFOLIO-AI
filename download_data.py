import yfinance as yf
import os

# List of Nifty companies
tickers = [
"RELIANCE.NS","HDFCBANK.NS","BHARTIARTL.NS","TCS.NS","ICICIBANK.NS","SBIN.NS",
"INFY.NS","HINDUNILVR.NS","LT.NS","BAJFINANCE.NS","MARUTI.NS","M&M.NS",
"KOTAKBANK.NS","ITC.NS","TITAN.NS","ASIANPAINT.NS","TATAMOTORS.NS","BAJAJ-AUTO.NS",
"NESTLEIND.NS","HINDALCO.NS","ADANIENT.NS","POWERGRID.NS","JSWSTEEL.NS",
"DIVISLAB.NS","INDUSINDBK.NS","UPL.NS","CIPLA.NS","BPCL.NS","APOLLOHOSP.NS",
"JIOFIN.NS","VEDL.NS","GRASIM.NS","EICHERMOT.NS","SBILIFE.NS","TATACONSUM.NS",
"PIDILITIND.NS","AMBUJACEM.NS","DRREDDY.NS","GAIL.NS","HEROMOTOCO.NS"
]

# Create data folder if doesn't exist
os.makedirs("data", exist_ok=True)

print("📥 Downloading raw price data...")

for ticker in tickers:
    try:
        df = yf.download(ticker, period="5y")
        df.to_csv(f"data/{ticker}.csv")
        print(f"✅ {ticker} saved")
    except Exception as e:
        print(f"❌ Failed for {ticker}: {e}")

print("✅ All data downloaded!")
