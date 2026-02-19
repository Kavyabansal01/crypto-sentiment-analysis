## Setup and How to Run

1. Clone repository
git clone https://github.com/Kavyabansal01/crypto-sentiment-analysis.git
cd crypto-sentiment-analysis

2. Create conda environment
conda create -n crypto-env python=3.10
conda activate crypto-env

3. Install dependencies
pip install -r requirements.txt

4. Run notebook
jupyter notebook

Open notebook.ipynb and run all cells.

Outputs will be saved in outputs/ folder.

# Crypto Sentiment Analysis

## Objective
This project analyzes how cryptocurrency trader behaviour changes under different market sentiment conditions using the Fear & Greed Index.

The goal is to understand:
- Does sentiment affect profitability?
- Do traders behave differently in Fear vs Greed markets?
- Can trading strategies be derived from behaviour patterns?

---

## Dataset
- Historical trading data (PnL, size, leverage, side, timestamp)
- Fear & Greed Index sentiment data

---

## Methodology
1. Cleaned and aligned timestamps
2. Converted sentiment to daily values
3. Merged trading data with sentiment data
4. Calculated metrics:
   - Average PnL
   - Win rate
   - Trade frequency
   - Position size
   - Leverage usage
5. Compared results across sentiment regimes
6. Segmented traders into behavioural groups

---

## Key Findings
- Traders earn highest profits during Extreme Greed markets
- Extreme Fear causes the largest losses
- Traders overtrade and over-leverage during Fear
- Very few traders are consistently profitable

---

## Strategy Recommendations
**Rule 1 — Defensive Trading**
Reduce leverage and trade frequency during Fear markets.

**Rule 2 — Trend Trading**
Follow momentum strategies during Greed markets.

---

## How to Run
Clone repository:
```bash
git clone https://github.com/your-username/crypto-sentiment-analysis.git
cd crypto-sentiment-analysis
