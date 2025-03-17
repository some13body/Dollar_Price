
from google import genai

client = genai.Client(api_key="AIzaSyBhgm9yc4fZeitQwWO6uAJO9Gs0ynP-l68")
response = client.models.generate_content(
    model="gemini-2.0-flash", contents="hey"
)
print(response.text)
