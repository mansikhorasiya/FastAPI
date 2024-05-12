from fastapi import FastAPI
from typing import Union
from enum import Enum
from pydantic import BaseModel
from fastapi import Query, Form


app = FastAPI()

class schema1(BaseModel):
    name: str
    Class: str
    roll_num: int

class choice_Names(str, Enum):
    one = "one"
    two = "two"
    three = "three"

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

@app.get("/query/")
async def query_func(roll_no: Union[int,None]=None ,name: Union[str,None]=None):
    var_name ={'name': name, 'roll_no':roll_no}
    return (var_name)


@app.get("/models/{model_name}")
async def get_model(model_name: choice_Names):
    if model_name.value == "one":
        return {"model_name": model_name, "message": "Calling One!"}

    if model_name.value == "two":
        return {"model_name": model_name, "message": "Calling two!"}

    return {"model_name": model_name, "message": "Calling three"}
    # return(model_name)

# Request body
@app.post("/items/")
async def create_item(item: schema1):
    return item

class mansi(BaseModel):
    one : str
    two :str
    three : int

# form data
@app.post("/form/data")
# async def form_data(username : str= Form(), password: str=Form()):
async def form_data(items: mansi):

    return({"items":items})

