import logging

from src.save_to_file import save_to_file
from src.news import get_news
import datetime


logger = logging.getLogger("main")
logger.setLevel(logging.INFO)
filehandler = logging.FileHandler("logs/main.log")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
filehandler.setFormatter(file_formater)
logger.addHandler(filehandler)


def main():
    try:
        logger.info("Request about user keywords")
        query = input("Введите ключевые слова: ")
        exclude_word = input("Введите слова-исключения: (через запятую) ").split(",")

        today = datetime.datetime.today()
        today_string = today.strftime("%Y-%m-%d")

        logger.info("Getting news")
        articles_list = get_news("tesla", exclude_word)

        logger.info("Write to the file")
        file_name = f'{today_string}_{query.replace(" ", "_")}.json'
        file_path = f"news/{file_name}"

        save_to_file(articles_list, file_path)
    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}")


if __name__ == "__main__":
    main()
