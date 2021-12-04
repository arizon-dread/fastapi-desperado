from typing import Optional, Text
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from .models.desperado import Desperado


app = FastAPI()
file = open("app/config/cors.txt", "r")
origins = file.read().split()

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
    responseText: str
    responseText = ""
    for c in request.text:
        responseText += getCharOrText(c)
    response = Desperado(text=responseText)
        
    return response

def getCharOrText(c):
    if (c in "bcdfghjklmnpqrstvxz"):
        return c+"o"+c
    elif (c in "BCDFGHJKLMNPQRSTVXZ"):
        return c+"o"+c.lower()
    else:
        return c
