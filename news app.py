import requests

NEWS_API_KEY = "YOUR_NEWS_API_KEY"
NEWS_API_ENDPOINT = "https://newsapi.org/v2/top-headlines"

def get_news(api_key, country="us"):
    params = {
        "apiKey": api_key,
        "country": country,
    }
    response = requests.get(NEWS_API_ENDPOINT, params=params)
    data = response.json()
    return data

def display_news(articles):
    for idx, article in enumerate(articles, start=1):
        print(f"{idx}. {article['title']}")
        print(article['description'])
        print(article['url'])
        print("=" * 40)

def main():
    print("Fetching latest news...\n")
    news_data = get_news(NEWS_API_KEY)

    if news_data.get("status") == "ok":
        articles = news_data.get("articles", [])
        display_news(articles)
    else:
        print("Failed to fetch news.")

if __name__ == "__main__":
    main()