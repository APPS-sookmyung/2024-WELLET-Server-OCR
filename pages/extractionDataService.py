import pytesseract
import cv2
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os


def ocrService():
    load_dotenv()
    path = os.getenv("FILE_PATH")

    pytesseract.pytesseract.tesseract_cmd = os.getenv("PYTESSERACT_PATH")

    image = cv2.imread(path)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    text = pytesseract.image_to_string(rgb_image, lang='kor+eng')
    return text