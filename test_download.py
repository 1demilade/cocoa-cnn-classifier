import requests
import os
MODEL_PATH = "DenseNet121_Cocoa_diagnosis.keras"
GDRIVE_URL = "https://drive.usercontent.google.com/download?id=1UtlCqjhyIP5kFP-6SZxvBIAicQfk_51X&export=download&authuser=0&confirm=t&uuid=f360f06c-1be4-4cbe-ad15-48b56f6e639b&at=AN8xHoo0DB2tdHStCx6b1qe-ZuXE%3A1749893051461"

def download_model():
    if not os.path.exists(MODEL_PATH):
        print("📥 Downloading model from Google Drive...")
        response = requests.get(GDRIVE_URL, stream=True)
        with open(MODEL_PATH, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print("✅ Model downloaded.")

download_model()