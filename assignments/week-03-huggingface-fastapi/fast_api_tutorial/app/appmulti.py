from fastapi import FastAPI
from pydantic import BaseModel
import transformers
import torch
from transformers import pipeline
from typing import List

traduction = pipeline("translation_en_to_fr", model = "model/gilles1")
#in "week-03-hugginface-fastapi/fast_api_tutorial/app/model/gilles1

app = FastAPI()



class TextsToTranslate(BaseModel):
    input_texts: List[str]


@app.get("/")
def index():
    return {"message": "Hello tata"}
    
@app.get("/ping")
def ping():
    return {"message": "alala"}

@app.post("/echo")
def echo(texts_to_translate: TextsToTranslate):
#    return {"message": text_to_translate.input_text}#
    return {"message":(traduction)(texts_to_translate.input_texts)}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("appmulti:app",
     host="0.0.0.0", port=8000, reload=True)