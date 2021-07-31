from starlette.routing import Route
from api.controllers import classification

api_routes = [
    Route('/classification', classification.classify, name="classificate_image", methods=["POST"]),
]