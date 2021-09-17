## startlette
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

from api.routes.routes import api_routes
from model.model import LOADED_MODEL
from api.config.logger import LOGGER
from api.config.settings import PROD

def startup():
    if PROD:
        LOADED_MODEL.load_model()
    LOGGER.info('Ready to go')

middleware = [
    Middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'])
]

app = Starlette(debug=True, 
                on_startup=[startup],
                routes=api_routes,
                middleware=middleware)
                