from flask import Flask, request, jsonify
from twilio.rest import Client
import os

app = Flask(__name__)

client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH"))

@app.route("/alert", methods=["POST"])
def alert():
    data = request.get_json(force=True)

    text = data.get("message", "🚨 Alert received")

    client.messages.create(
        body=text,
        from_=os.getenv("TWILIO_NUMBER"),
        to=os.getenv("MY_NUMBER")
    )

    return jsonify({"status": "SMS sent"}), 200

@app.route("/")
def health():
    return "✅ Alert service running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
