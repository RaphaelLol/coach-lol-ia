from flask import Flask, request, jsonify
import rofl_parser  # librairie qui lit directement les fichiers .ROFL

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload_replay():
    file = request.files["file"]

    # Parse le fichier ROFL
    replay_data = rofl_parser.parse(file)

    # Retourne le JSON directement
    return jsonify(replay_data)

if __name__ == "__main__":
    app.run()
