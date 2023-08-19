import json
import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

API_URL = "https://api-inference.huggingface.co/models/gpt2"
HUGGING_FACE_TOKEN = os.getenv("HUGGING_FACE_TOKEN")
headers = {"Authorization": f"Bearer {HUGGING_FACE_TOKEN}"}

def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))
data = query("Can you please let us know more details about your ")
print(data)