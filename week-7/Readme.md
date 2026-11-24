In Week 7, I created a next-token predictor to see how a language model chooses the next word. It takes a sentence, shows its tokens, and displays the 10 most likely next tokens with their probabilities and logits.

**How I did it:**

Loaded a small pretrained model (distilgpt2) with Hugging Face Transformers.

Converted the input sentence into tokens.

Ran the model to get the logits for the last position.

Converted the logits into probabilities using softmax.

Picked the top 10 candidates using top-k.

Printed each token with its probability and logit.

Plotted a bar chart of the top 10 next-token probabilities using Matplotlib.

**Commands used:**

cd week-7

pip install -r requirements.txt

python next_token.py
