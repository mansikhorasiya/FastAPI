from fastapi import FastAPI
from sqlalchemy.orm import Session

import models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.get("/")
def cheking():
    return("Hello....")
