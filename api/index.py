from fastapi import FastAPI
from api.utils.pdf_csv import convert_pdfs_csv


app = FastAPI()


@app.get("/api/convert-pdfs")
def pdf_csv():
    result = convert_pdfs_csv()
    return result
