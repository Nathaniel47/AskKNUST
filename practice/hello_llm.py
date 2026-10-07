from dotenv import load_dotenv
from google import genai

load_dotenv()              # loads GEMINI_API_KEY from .env
client = genai.Client()    # picks up the key automatically

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Explain retrieval-augmented generation in two sentences.",
)
print(response.text)