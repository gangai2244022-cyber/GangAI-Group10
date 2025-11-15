from flask import Flask, request, jsonify
import random
from datetime import datetime

app = Flask(__name__)

GANGES_FACTS = [
    "The Ganges shark is one of the few true freshwater sharks.",
    "The Ganges shark is critically endangered due to human activities.",
    "Very few confirmed sightings exist in the last decades.",
    "The Ganges shark lives mostly in the Ganges–Brahmaputra system.",
    "Scientists know very little about how this shark reproduces."
]

def greeting():
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "Good morning!"
    elif 12 <= hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"

@app.route("/webhook", methods=["POST"])
def webhook():
    req = request.get_json()

    intent = req["queryResult"]["intent"]["displayName"]

    if intent == "Welcome Intent":
        text = f"{greeting()} I'm GangAI. Ask me about the Ganges shark!"
        return jsonify({"fulfillmentText": text})

    if intent == "GangesShark RandomFact":
        fact = random.choice(GANGES_FACTS)
        return jsonify({"fulfillmentText": f"Here's a fact: {fact}"})

    return jsonify({"fulfillmentText": "I'm not sure, but I'm learning!"})

if __name__ == "__main__":
    app.run(port=5000, debug=True)