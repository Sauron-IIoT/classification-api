from tensorflow import keras
from api.config.logger import LOGGER


class ClassificationModel():
    def __init__(self, h5_file_path):
        self.path = h5_file_path
        self.model = None

    def load_model(self):
        try:
            LOGGER.info("Loading model from: {}".format(self.path))
            self.model = keras.models.load_model(filepath=self.path)
            LOGGER.info("Model loaded succesfully")
        except Exception as exc:
            LOGGER.fatal(exc)

LOADED_MODEL = ClassificationModel("model/weights/model_box.h5")