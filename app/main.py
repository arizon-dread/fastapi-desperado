from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Desperado(BaseModel):
    text: str


app = FastAPI()

@app.get('/')
def root():
    return {"hello world"}

@app.post('/desperado')
async def transform(content: Desperado):
    newText=""
    for c in content.text:
        newText += getCharOrText(c)
    return newText

def getCharOrText(c):
    if (c in "bcdfghjklmnpqrstvxz"):
        return c+"o"+c
    elif (c in "BCDFGHJKLMNPQRSTVXZ"):
        return c+"O"+c
    else:
        return c
