## startlette
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

from typing import Optional
from starlette.routing import Route
from starlette.applications import Starlette
from pydantic import BaseModel, constr
from starlette_pydantic import PydanticEndpoint, BaseForm
from starlette_openapi import OpenApi
from starlette_swagger import SwaggerUI
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.middleware import Middleware
from starlette.authentication import (
    AuthenticationBackend, AuthenticationError, SimpleUser, UnauthenticatedUser,
    AuthCredentials
)
from starlette_authentication.decorators import requires, token_url
import base64
import binascii

from api.routes.routes import api_routes

def startup():
    print('Ready to go')

middleware = [
    Middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'])
]

app = Starlette(debug=True, 
                on_startup=[startup],
                routes=api_routes,
                middleware=middleware)

openapi = OpenApi(app, title="Demo", description="swagger ui demo.")
SwaggerUI(app, openapi)
                