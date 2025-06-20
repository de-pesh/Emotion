from transformers import pipeline

# Load model once at startup
emotion_classifier = pipeline("sentiment-analysis")

def detect_emotion(text):
    result = emotion_classifier(text)[0]
    label = result['label']
    score = result['score']
    
    if label == 'POSITIVE':
        emotion = "Happy/Positive"
    elif label == 'NEGATIVE':
        emotion = "Sad/Negative"
    else:
        emotion = "Neutral"
    
    return {"emotion": emotion, "confidence": round(score, 2)}