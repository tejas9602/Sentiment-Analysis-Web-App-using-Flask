from flask import Flask, render_template, request
from textblob import TextBlob
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=os.path.join(BASE_DIR, "templates"))

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = None
    if request.method == "POST":
        text = request.form.get("text")
        analysis = TextBlob(text)
        sentiment = analysis.sentiment
    return render_template("index.html", sentiment=sentiment)

if __name__ == "__main__":
    app.run(debug=True)
