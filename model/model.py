from tensorflow import keras
from api.config.logger import LOGGER

LOADED_MODEL = None

def load_model(file_path):
    try:
        LOGGER.info("Loading model from: {}".format(file_path))
        # LOADED_MODEL = 
    except Exception as exc:
        print(exc)
