from fastapi import FastAPI
<<<<<<< HEAD
from pydantic import BaseModel
import transformers
import torch
from transformers import pipeline
#    pipeline("translation_en_to_fr", model = "fast_api_tutorial/app/model/gilles1")
traduction = pipeline("translation_en_to_fr", model = "model/gilles1")

app = FastAPI()

class TextToTranslate(BaseModel):
    input_text: str



@app.get("/")
def index():
    return {"message": "Hello toto"}
    
@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.post("/echo")
def echo(text_to_translate: TextToTranslate):
#    return {"message": text_to_translate.input_text}#
    return {"message":traduction(text_to_translate.input_text)}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app",
     host="0.0.0.0", port=8000, reload=True)
=======

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello World"}
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
>>>>>>> 246ef8a5e00ef3fdec5d8736d02d9e066943f171
