import os
import requests
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
if not token:
    raise RuntimeError("HUGGINGFACEHUB_API_TOKEN not set or not loaded")

model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"  # replace with the exact model you intend to call
url = f"https://api-inference.huggingface.co/models/{model_id}"
headers = {"Authorization": f"Bearer {token}"}

resp = requests.get(url, headers=headers)
print("Status:", resp.status_code)
print("Response:", resp.text[:1000])  # truncated for readability
