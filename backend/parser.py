import zipfile
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Coach LoL Backend is running 🚀"


@app.route("/upload", methods=["POST"])
def upload_replay():
    file = request.files["file"]

    # Ouvrir le fichier ROFL comme un zip
    with zipfile.ZipFile(file) as z:
        with z.open("replay.json") as replay_file:
            replay_data = json.load(replay_file)

    return jsonify(replay_data)

if __name__ == "__main__":
    app.run()

