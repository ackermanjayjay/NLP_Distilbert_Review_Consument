from typing import Union

from fastapi import FastAPI
from model_initiation import predict
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/prediction/{text}")
def read_item(text:str, query:str):
    return {
        "input_text":query,
        "result":predict(query)
    }
