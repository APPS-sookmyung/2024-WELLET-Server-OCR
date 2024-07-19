from fastapi import FastAPI

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from pages import train_data
import json

app = FastAPI()

@app.get("/health")
def root():
    return {"message" : "WELLET Server OCR Health Check"}

@app.get("/ocr")
def ocr():
    result = {'result': train_data.ocrService()}
    return result
    