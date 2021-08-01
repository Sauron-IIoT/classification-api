from tensorflow import keras
from api.config.logger import LOGGER

LOADED_MODEL = None

def load_model(file_path):
    try:
        LOGGER.info("Loading model from: {}".format(file_path))
        LOADED_MODEL = keras.models.load_model(filepath=file_path)
        LOGGER.info("Model loaded succesfully")
    except Exception as exc:
        LOGGER.fatal(exc)
