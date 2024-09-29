import datetime

from src.config import API_KEY, BASE_URL
import requests


def get_news(query, exclude_words, api_key = API_KEY):
    today = datetime.datetime.today()

    params = {"q" : query,
              # "from" : today.strftime('%Y-%m-%d'),
              "sortBy" : "publishedAt",
              "apiKey" : api_key
              }
    try:
        response = requests.get(BASE_URL, params=params)
        news_data = response.json()
        if news_data.get('status') != 'ok':
            return []
        articles_list = news_data.get('articles', [])
        articles_result = []
        for article in articles_list:
            content = f'{article.get("title")} {article.get("description")}'.lower()
            if any(word in content for word in exclude_words):
                continue
            articles_result.append({
                    'title' : article.get('title'),
                    'author' : article.get('author'),
                    'description' : article.get('content'),
                    'url' : article.get('url')
                })
        return articles_result
    except requests.RequestException:
        return []
    except Exception:
        return []
