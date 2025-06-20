from flask import Flask, render_template, request
from emotion_detector import detect_emotion

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    emotion_result = None
    if request.method == "POST":
        user_text = request.form["text"]
        emotion_result = detect_emotion(user_text)
    return render_template("index.html", result=emotion_result)