from typing import Optional, Text
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from app.handlers.dateToSeconds import DateToSeconds

from app.models.birthdaySeconds import BirthdaySeconds
from .models.desperado import Desperado
from .handlers.textManipulator import TextManipulator


app = FastAPI()
file = open("app/config/cors.txt", "r")
origins = file.read().split(";")

print(origins)

app.add_middleware(
    CORSMiddleware, 
    allow_origins = origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

@app.get('/api')
def root():
    return {"hello world"}

@app.post('/api/desperado', response_model=Desperado)
async def transform(request: Desperado):
    responseText: str = ""
    textMnpltr = TextManipulator()
    responseText = textMnpltr.transform(request)
    return responseText

@app.post('/api/birthdaySeconds', response_model=BirthdaySeconds)
async def birthdaySeconds(request: BirthdaySeconds):
    dateToSeconds = DateToSeconds()
    request.birthdaySeconds = dateToSeconds.getSeconds(request.birthday)
    return request