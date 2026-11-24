In Week 5, I created a budget calculator to estimate the cost of using an LLM API. It calculates daily and monthly token usage and API costs.

**How I did it:**

Created a FeatureBudget class.

Calculated input and output tokens per day.

Estimated daily and monthly API costs.

Checked RPM and TPM limits.

Checked daily and monthly budgets.

Added unit tests to verify the calculations.

**Commands used:**

cd week-5

pip install -r requirements.txt

python budget.py

python -m unittest test_budget.py
