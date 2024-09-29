import json
import logging

logger = logging.getLogger("save_to_file")
logger.setLevel(logging.INFO)
filehandler = logging.FileHandler("logs/save_to_file.log")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
filehandler.setFormatter(file_formater)
logger.addHandler(filehandler)


def save_to_file(data, file_path):
    try:
        logger.info(f"Write data to the file {file_path}")
        with open(file_path, "w") as data_file:
            json.dump(data, data_file)
    except Exception as ex:
        logger.error(f"Happened the error {ex}")
        pass
