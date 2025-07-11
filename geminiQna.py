import os
import requests
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variable's
load_dotenv()

SERPAPI_KEY = os.getenv("SERPAPI_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.0-pro-exp')

def google_search(query):
    
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_KEY
    }
    
    response = requests.get("https://serpapi.com/search", params=params)
    results = response.json()
    
    if "organic_results" in results:
        return "\n".join([res["snippet"] for res in results["organic_results"][:5]])
    return "No results found."

def chat_with_gemini(query):
    
    search_results = google_search(query)
    
    prompt = f"""I searched Google for "{query}" and found the following information:
    {search_results}
    
    Based on this, please give me a concise and to-the-point answer."""
    
    response = model.generate_content(prompt)
    return response.text.replace("*", "") 