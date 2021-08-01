## startlette
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

from api.routes.routes import api_routes
from model.model import load_model
from api.config.logger import LOGGER

def startup():
    load_model("blabla/zzzzzzzz")
    LOGGER.info('Ready to go')

middleware = [
    Middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'])
]

app = Starlette(debug=True, 
                on_startup=[startup],
                routes=api_routes,
                middleware=middleware)
                