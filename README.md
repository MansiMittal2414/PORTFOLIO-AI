# portfolio-ai — Supplementary materials for paper "AI-based Portfolio Optimization"

## Contents
- `analysis/` — scripts for CAPM, MVO, KMeans, comparisons.
- `models/` — LSTM & traditional models.
- `RL_portfolio/` — RL environment and training/evaluation scripts.
- `data/` — price and returns CSVs used.
- `results/` — final plots, metrics, and best RL model zip.

## Reproduce key figures
1. Create virtualenv and install: `python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt`
2. Run LSTM predictions: `python3 models/lstm_weights.py`
3. Train RL (optional): `python3 RL_portfolio/train.py`
4. Generate comparison plot: `python3 analysis/make_comparison_figure.py`
5. Extract metrics table: `python3 analysis/extract_metrics.py`

## Files to include in paper
- `results/all_strategies_comparison.png` (Figure)
- `results/strategy_metrics_table.csv` (Table)
- `results/efficient_frontier.png` (Figure)
