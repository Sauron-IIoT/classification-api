import os
from starlette.config import Config

# Config will be read from environment variables and/or ".env" files.
__config = Config(".env")

PROD = os.getenv("PROD") if os.getenv("PROD") != None else __config('PROD', cast=bool, default=False)
MODEL_PATH = os.getenv("MODEL_PATH") if os.getenv("MODEL_PATH") != None else __config('MODEL_PATH', cast=str, default="model/weights/model_apple_banana.h5")