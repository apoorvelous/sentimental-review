from flask import Flask, render_template, request, jsonify
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/sentiment-analysis", methods=["POST"])
def sentiment_analysis():
    feedback = request.json.get("feedback")
    if not feedback:
        return jsonify({
            "error": "Feedback cannot be empty!"
        }), 400
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(feedback)
    score = round((((ss.get("compound")+1)/2)*100) / 20, 2)
    return jsonify({"data": score}), 200

if __name__ == '__main__':
	app.run()
