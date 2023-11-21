from fastapi import FastAPI
from api.utils.download_drive_ep import download_drive_ep


app = FastAPI()


@app.get("/api/download_drive_ep")
def trigger_download():
    result = download_drive_ep()
    return result
