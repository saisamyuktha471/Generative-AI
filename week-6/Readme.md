In Week 6, I created a baseline evaluation for an LLM using a golden question set. It asks the model 30 questions about tokenization, text generation, embeddings and positional encoding. It scores each answer by keyword coverage and saves the results to a CSV file.

**How I did it:**

Created a golden set (golden_set.json) of 30 questions with expected answers, keywords and sources.

Ran the local Ollama model (llama3.2) with temperature 0 to get consistent answers.

Calculated a keyword score for each answer from the matched and missing keywords.

Marked each question PASS if the score was 60% or higher, otherwise REVIEW (or ERROR if the request failed).

Saved the question, answers, keywords, score, status, model and release (v0.1) to baseline_results.csv.

Printed a baseline summary. The result was 13 PASS, 17 REVIEW and an average keyword coverage of 52.78%.

**Commands used:**

cd week-6

pip install -r requirements.txt

ollama run llama3.2 (the Ollama server must be running)

python main.py
