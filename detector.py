import requests
import os

API_URL = "https://api-inference.huggingface.co/models/bhadresh-savani/distilbert-base-uncased-emotion"
headers = {"Authorization": f"Bearer {os.getenv('HF_API_TOKEN')}"}

def detect_emotion(text):
    payload = {"inputs": text}
    response = requests.post(API_URL, headers=headers, json=payload)
    result = response.json()

    try:
        top_result = result[0][0]
        return {"emotion": top_result["label"], "confidence": round(top_result["score"], 2)}
    except:
        return {"emotion": "Error", "confidence": 0.0}