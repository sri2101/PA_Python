import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def fetch_news():
    
    try:
        params = {
            "engine": "google_news",
            "q": "latest news",
            "api_key": SERPAPI_KEY
        }
        response = requests.get("https://serpapi.com/search", params=params)
        data = response.json()
        
        if "news_results" in data:
            news_articles = data["news_results"][:5]  # Fetch top 5 news articles
            return [f"- {article['title']} ({article['link']})" for article in news_articles]
        else:
            return ["No news data found."]
    except Exception as e:
        return [f"Error fetching news data: {str(e)}"]
