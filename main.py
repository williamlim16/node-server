from fastapi import FastAPI, File, UploadFile
# import requests
import aiofiles

app = FastAPI()

RemoteServer = '127.0.0.1:3001'


@app.get("/")
async def root():
    return {"message": "hellowwwoooo"}


@app.post("/api/upload")
async def create_upload_file(file: UploadFile):
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
    return {"filename": file.filename}
