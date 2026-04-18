from flask import Flask, render_template, request, jsonify
from encryption import encrypt_message, decrypt_message

app = Flask(__name__)

messages = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    data = request.json
    msg = data["message"]
    key = data["key"]

    encrypted = encrypt_message(msg, key)
    messages.append(encrypted)

    return jsonify({"encrypted": encrypted})

@app.route("/receive", methods=["POST"])
def receive():
    key = request.json["key"]

    decrypted_messages = []
    for msg in messages:
        try:
            decrypted_messages.append(decrypt_message(msg, key))
        except:
            decrypted_messages.append("❌ Wrong Key")

    return jsonify({"messages": decrypted_messages})

if __name__ == "__main__":
    app.run(debug=True)