from numpy import random
from starlette.responses import JSONResponse
import logging
from tensorflow import keras
import tensorflow as tf
import numpy as np
from api.config.logger import LOGGER
import datetime


from api.messages.messages import Messages
from api.config.settings import PROD

from model.model import LOADED_MODEL

threshold = 0.7

labels = {
    0: "esp32",
    1: "motor",
}

async def classify(request):

    start_time = datetime.datetime.now()

    LOGGER.info(request)

    image_path = None

    try:
        input_data = await request.json()
        image_path = input_data["image"]
    except:
        print("Bad request")
        return JSONResponse({"Error": Messages.BAD_REQUEST.value}, status_code=400)

    logging.info(f'image path: {image_path}')

    prediction = None
    if PROD:
        prediction = predict(image_path)
    else:
        prediction = mock_predict()

    end_time = datetime.datetime.now()
    time_diff = (end_time - start_time)
    execution_time = time_diff.total_seconds() * 1000
    prediction['prediction_processing_time'] = execution_time

    LOGGER.info(f'prediction: {prediction}')

    return JSONResponse(content=prediction, status_code=200)


def mock_predict():
    return { "label": labels[random.randint(0, 1)], "confidence": random.random() }

def predict(image_path):

    print(f'loading image {image_path}')

    image = load_img(image_path)

    logging.info('image loaded')

    prediction = LOADED_MODEL.model.predict(image)[0]

    logging.info(f'model prediction: {prediction}')

    max_class = np.argmax(prediction)
    max_confidence = float(np.max(prediction))

    if (max_confidence < threshold):
        return { "label": None, "confidence": None }
    else:
        return { "label": labels[max_class], "confidence": max_confidence }

def load_img(image_path):
    image = keras.preprocessing.image.load_img(
        image_path, target_size=(320, 480)
    )
    img_array = keras.preprocessing.image.img_to_array(image)
    img_array = tf.expand_dims(img_array, 0)
    return img_array / 255.
