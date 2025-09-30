import requests
from src.config import NEWS_API_KEY

def fetch_news(topic : str, language: str="en", page_size : int = 20):
    # This functions fetched news articles from NewsAPI based on a topic.
    url = (
        "https://newsapi.org/v2/everything?"
        f'q={topic}&'
        f"language={language}&"
        f"pageSize={page_size}&"
        f"apiKey={NEWS_API_KEY}"
    )
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(f"Successfully fetched {len(data.get('articles', []))} articles for topic: '{topic}'")
        return data.get('articles', [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from NewsAPI: {e}")
        return []

