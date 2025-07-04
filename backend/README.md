# 🛡️ PII Masker - FastAPI Backend

A FastAPI application that detects and masks Personally Identifiable Information (PII) from uploaded images using OCR and PII detection.

## 📦 Features

- Upload image files (e.g., JPG, PNG)
- Extract text using OCR
- Detect PII in the text
- Mask detected PII on the image
- Stream the masked image back to the client
- CORS enabled for local and ngrok frontend access


## 🚀 Getting Started

1. Clone the Repo

```bash
git clone https://github.com/your-username/pii-masker.git
cd pii-masker/backend
```
2. Create Virtual Environment
```bash
python -m venv env
.\env\Scripts\activate  
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```

4. Run the Server
```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

5. Test the API
```bash
POST http://127.0.0.1:8000/docs/mask-pii
```




