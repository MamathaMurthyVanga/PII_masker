
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import shutil
import os
from utils.ocr import extract_text_with_boxes
from utils.pii_detector import detect_pii
from utils.masker import mask_pii_on_image
from fastapi.middleware.cors import CORSMiddleware


from fastapi.responses import StreamingResponse
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://localhost:3000","https://f29a-115-98-181-49.ngrok-free.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/mask-pii")
async def mask_pii(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    ocr_results = extract_text_with_boxes(file_path)
    masked_image_path = mask_pii_on_image(file_path, ocr_results, detect_pii)

    # Read masked image into memory as bytes
    with open(masked_image_path, "rb") as img_file:
        image_bytes = io.BytesIO(img_file.read())

    return StreamingResponse(image_bytes, media_type="image/jpeg", headers={"Content-Disposition": "inline; filename=masked.jpg"})

    # return FileResponse(masked_image_path, media_type="image/jpeg", filename="masked_" + file.filename)

# to run
# uvicorn main:app --reload --host 127.0.0.1 --port 8000
# uvicorn main:app --reload

