from fastapi import FastAPI, File, UploadFile, Form
# import requests
import aiofiles
import paho.mqtt.client as mqtt
import time

app = FastAPI()

RemoteServer = '127.0.0.1:3001'


@app.get("/")
async def root():
    return {"message": "hellowwwoooo"}


@app.post("/api/upload")
async def create_upload_file(file: UploadFile, trashcan: str = Form(...), image: str = Form(...)):

    mqttBroker = "127.0.0.1"
    client = mqtt.Client("publisher")
    client.connect(mqttBroker)
    async with aiofiles.open(file.filename, 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)

    # payload = {
    #     'classified':'test',
    #     'trashcanid':1,
    #     'image':file
    # }
    # session = requests.session()
    # r.requests.post(RemoteServer+'',data=payload )

    client.publish(trashcan, "banana")
    print("just published " + image + " for " + trashcan)
    return {"filename": file.filename}
