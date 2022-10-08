import logging
import os

from deploying_ml_models.config import (
    INPUT_DATA_DIR,
    FILE_DIR,
    INPUT_DIR,
    CONFIG_DIR,
    MODELS_DIR,
    LOGGING_DIR,
    OUTPUT_DIR,
    OUTPUT_DATA_DIR,
)

logger = logging.getLogger(__name__)


def create_folders(folder_list):
    folder_list.insert(0, FILE_DIR)
    for folder in folder_list:
        try:
            os.mkdir(folder)
            print(f"Created folder with path: {folder}")
        except FileExistsError:
            print(f"Folder already exists for path: {folder}")


if __name__ == "__main__":
    folders_to_be_created = [
        FILE_DIR,
        LOGGING_DIR,
        INPUT_DIR,
        CONFIG_DIR,
        MODELS_DIR,
        INPUT_DATA_DIR,
        OUTPUT_DIR,
        OUTPUT_DATA_DIR,
    ]

    create_folders(folders_to_be_created)
