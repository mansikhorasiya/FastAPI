from fastapi import FastAPI
from typing import Union
from enum import Enum
from pydantic import BaseModel
from fastapi import Query, Form , File, UploadFile, HTTPException


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

# file upload
@app.post("/file/upload")
async def file_bytes_len(file: bytes = File()):
    return ({'file':len(file)})

@app.post("/upload/file")
async def file_upload(file: UploadFile):
    # return ({'file':file})
    return({"file_name": file.filename, "file_content_name": file.content_type})

@app.post("/formdata/uploadfile")
async def formdatauploadfile(file1: UploadFile,file2 :bytes = File(), name: str = Form()):
    return({"file_name": file1.filename, "file2_bytes": len(file2),"name": name})


items = [1,2,3,4,5]

# error handling
@app.get("/error/handling")
async def handle_error(item: int):
    if item not in items:
        return HTTPException(status_code= 400, detail="Item is not eqal to 2 try another value!!!")
    return {"value": item}

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

#  Declare request example data.
    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }
