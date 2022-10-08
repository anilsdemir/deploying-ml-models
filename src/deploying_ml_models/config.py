from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent

FILE_DIR = Path.joinpath(BASE_DIR, "local")

LOGGING_DIR = Path.joinpath(FILE_DIR, "logs")

MODELS_DIR = Path.joinpath(FILE_DIR, "models")

INPUT_DIR = Path.joinpath(FILE_DIR, "inputs")

INPUT_DATA_DIR = Path.joinpath(INPUT_DIR, "data")

CONFIG_DIR = Path.joinpath(INPUT_DATA_DIR, "config")

OUTPUT_DIR = Path.joinpath(FILE_DIR, "outputs")

OUTPUT_DATA_DIR = Path.joinpath(OUTPUT_DIR, "data")
