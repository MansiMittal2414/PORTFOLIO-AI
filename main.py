from utils.preprocessing import load_price_data, load_returns
from models.lstm_model.py import run_lstm
from models.unsupervised_model import run_unsupervised
from models.traditional_models import run_traditional
from backtest.rolling_backtest import backtest_strategy
from utils.metrics import sharpe_ratio, max_drawdown

# STEP 1: Load data
try:
    prices, returns = load_returns()
except:
    prices = load_price_data()
    prices, returns = load_returns()

# STEP 2: Run models
lstm_pred = run_lstm(prices)
clusters = run_unsupervised(returns)
traditional_weights = run_traditional(prices)

# STEP 3: Backtest traditional strategy
tr_returns, tr_curve = backtest_strategy(traditional_weights, returns)

# STEP 4: Results
print("Sharpe:", sharpe_ratio(tr_returns))
print("Max Drawdown:", max_drawdown(tr_curve))
print("Traditional Sample Weights:", traditional_weights)
