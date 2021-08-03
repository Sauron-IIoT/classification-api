from starlette.responses import JSONResponse
from datetime import datetime
import pytz
import logging

from api.messages.messages import Messages
from api.model.response import Response

from model.model import LOADED_MODEL
from model import utils

import matplotlib.image as mpimg

threshhold = 0.7
de_para = {
    1: "opened",
    0: "closed",
}


async def classify(request):

    image_path = None
    new_w = 416
    new_h = 416
    started_time = datetime.now(pytz.timezone("Etc/GMT+3")).strftime('%Y:%m:%d %H:%M:%S %Z %z')
    
    try:
        #input_data with keys: name, tag
        input_data = await request.json() 
        image_path = input_data["image"]       
    except:
        print("Bad request")
        return JSONResponse({"Error": Messages.BAD_REQUEST.value}, status_code=400)

    # pega o modelo, classifica
    image = None
    try:
        logging.info(image_path)
        image = mpimg.imread(image_path)
    except Exception as exc:
        logging.fatal(exc)
        return JSONResponse({"Error": str(exc)}, status_code=500)

    image_resized = utils.preprocess_input(image, new_w, new_h)
    score = LOADED_MODEL.model.predict(image_resized).reshape((1))[0]
    score_binario = 1 if score > threshhold else 0

    response = Response(str(score), str(score_binario), de_para[score_binario], started_time).response

    return JSONResponse(content=response, status_code=200)