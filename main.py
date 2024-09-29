from src.news import get_news


def main():
    articles = get_news('tesla', ['T-Rex'])
    print(articles)



if __name__ == "__main__":
    main()