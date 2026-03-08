from fastapi import APIRouter, File, UploadFile
import shutil
from typing import List

upload_router = APIRouter()

@upload_router.post("/file")
def upload_file(file: bytes = File()):
    return {
        "file_size" : len(file)
    }

@upload_router.post("/upload_file1")
def upload_file1(file: UploadFile):
    return {
        "filename" : file.filename,
        "content_type" : file.content_type
    }

@upload_router.post("/upload_file2")
def upload_file2(file: UploadFile):

    with open("img/image.jpeg", "wb") as buffer: #wb modo escritura de byte
        shutil.copyfileobj(file.file, buffer)
        buffer = file.file

    return {
        "filename" : file.filename,
    }


@upload_router.post("/upload_file3")
def upload_file3(images: List[UploadFile] = File()):

    for image in images:
        with open("img/"+image.filename, "wb") as buffer: 
            shutil.copyfileobj(image.file, buffer)
 
