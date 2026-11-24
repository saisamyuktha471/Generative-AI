In Week 2, I created a common LLM client to work with different AI models. I added Gemini and Ollama as two providers. The user can select a provider and ask questions.

**How I did it:**

Created an abstract class called LLMProvider.

Implemented GeminiProvider and OllamaProvider.

Created LLMClient to handle both providers.

Added a test file to check the client.

**Commands used:**

cd week-2

pip install -r requirements.txt

python main.py

python -m unittest test_client.py
