from fastapi import FastAPI

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from pages import extractionDataService, extractRegularService
from dto.ResultExtraction import ResultExtraction

app = FastAPI()

@app.get("/health")
def root():
    return {"message" : "WELLET Server OCR Health Check"}

@app.get("/data")
def extractionData():
    result = {'result': extractionDataService.ocrService()}
    return result

@app.post("/regular")
def extractRegular(text: ResultExtraction):
    extractRegularService.regular(text)
    return text
    # return {'name': name, 'position': position, 'email': email, "phone": phone, "tel": tel, "department": department, "company": company, "address": address}