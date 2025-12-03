from flask import Flask, request, jsonify
from datanashor.parser import ReplayParser

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload_replay():
    file = request.files["file"]  # fichier envoyé par le frontend
    parser = ReplayParser()
    replay = parser.parse(file)

    data = {
        "gameLength": replay.get("gameLength"),
        "gameMode": replay.get("gameMode"),
        "mapId": replay.get("mapId"),
        "players": [
            {
                "summonerName": p.get("summonerName"),
                "championName": p.get("championName"),
                "lane": p.get("lane")
            }
            for p in replay.get("players", [])
        ],
        "events": replay.get("events", [])
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
