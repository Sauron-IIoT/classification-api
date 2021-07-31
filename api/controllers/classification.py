from starlette.responses import JSONResponse
from api.messages.messages import Messages
from api.model.response import Response

async def classify(request):

    image_path = None
    try:
        #input_data with keys: name, tag
        input_data = await request.json() 
        image_path = input_data["image"]       
    except:
        print("Bad request")
        return JSONResponse({"Error": Messages.BAD_REQUEST}, status_code=400)

    # pega o modelo, classifica

    return JSONResponse(content=Response(.95, 1, "opened").toJson(), status_code=200)