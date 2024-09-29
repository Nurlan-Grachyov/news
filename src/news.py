import datetime
import logging
from src.config import API_KEY, BASE_URL
import requests

logger = logging.getLogger("news")
logger.setLevel(logging.INFO)
filehandler = logging.FileHandler("logs/news.log")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
filehandler.setFormatter(file_formater)
logger.addHandler(filehandler)


def get_news(query, exclude_words, api_key=API_KEY):
    today = datetime.datetime.today()

    params = {
        "q": query,
        # "from" : today.strftime('%Y-%m-%d'),
        "sortBy": "publishedAt",
        "apiKey": api_key,
    }
    try:
        logger.info(f"Executing a query with keywords: {query}")
        response = requests.get(BASE_URL, params=params)
        news_data = response.json()
        if news_data.get("status") != "ok":
            logger.info("Статей не нашлось")
            return []
        articles_list = news_data.get("articles", [])
        articles_result = []
        logger.info(
            f'Filtering the query by exception messages: {", ".join(exclude_words)}'
        )
        for article in articles_list:
            content = f'{article.get("title")} {article.get("content")}'.lower()
            if any(word.lower() in content for word in exclude_words):
                continue
            articles_result.append(
                {
                    "title": article.get("title"),
                    "author": article.get("author"),
                    "description": article.get("content"),
                    "url": article.get("url"),
                }
            )
        return articles_result
    except requests.RequestException as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return []
    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return []
