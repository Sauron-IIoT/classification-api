from numpy import random
from starlette.responses import JSONResponse
from datetime import datetime
import pytz
import logging

from api.messages.messages import Messages
from api.model.response import Response
from api.config.settings import PROD

from model.model import LOADED_MODEL
from model import utils

import matplotlib.image as mpimg

threshhold = 0.5
de_para = {
    1: "banana",
    0: "apple",
}


async def classify(request):

    image_path = None
    new_w = 256
    new_h = 256
    started_time = datetime.now(pytz.timezone("Etc/GMT+3")).strftime('%Y:%m:%d %H:%M:%S %Z %z')
    
    try:
        input_data = await request.json() 
        image_path = input_data["image"]       
    except:
        print("Bad request")
        return JSONResponse({"Error": Messages.BAD_REQUEST.value}, status_code=400)

    score = 0
    if PROD:
        score = classify_img(image_path, new_w, new_h)
    else:
        score = mock_score()

    score_binario = 1 if score > threshhold else 0

    response = Response(str(score), str(score_binario), de_para[score_binario], started_time).response

    return JSONResponse(content=response, status_code=200)


def mock_score():
    return random.random()

def classify_img(image_path, new_width, new_height):
    image = None
    try:
        logging.info(image_path)
        image = mpimg.imread(image_path)
    except Exception as exc:
        logging.fatal(str(exc))
        raise exc

    image_resized = utils.preprocess_input(image, new_width, new_height)
    return LOADED_MODEL.model.predict(image_resized)[0][0].reshape(1)[0]