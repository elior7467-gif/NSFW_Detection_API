import os
os.environ["TF_USE_LEGACY_KERAS"] = "1"

from fastapi import FastAPI
from nsfw_detector import predict

app = FastAPI()
