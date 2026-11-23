In Week 3, I added monitoring features to track LLM usage. I collected input tokens, output tokens, response time and estimated API cost. I also stored the usage details in MongoDB.

**How I did it:**

Updated the LLM client to track token usage.

Calculated response time and estimated cost.

Added retry handling for temporary errors.

Created usage_logger.py to store usage details in MongoDB.

**Commands used:**

cd week-3

pip install -r requirements.txt

python main.py

python -m unittest test_client.py
