from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # autoriser ton frontend (GitHub Pages) à appeler l’API

@app.route("/")
def home():
    return "Coach LoL Backend is running 🚀"

# Si tu gardes l'upload .ROFL pour plus tard
# @app.route("/upload", methods=["POST"])
# def upload():
#     # TODO: parsing .ROFL si besoin
#     return jsonify({"status": "ok"})

@app.route("/analyze", methods=["POST"])
def analyze():
    """
    Corps attendu (JSON):
    {
      "timestamp": 900,
      "context": { "source": "video", "duration": 1800, ... }
    }
    """
    data = request.get_json(silent=True) or {}
    ts = data.get("timestamp")
    context = data.get("context", {})

    if ts is None:
        return jsonify({"error": "timestamp manquant"}), 400

    # Placeholder IA: règles simples selon le moment de la partie
    advice = simple_coach(ts, context)
    return jsonify({"advice": advice, "timestamp": ts})

def simple_coach(ts, context):
    # Exemples basiques que tu remplaceras par ta vraie IA
    if ts < 600:
        return "Early game: concentre-toi sur le last-hit, évite les trades défavorables et garde la wave côté sûr."
    elif ts < 1200:
        return "Mid game: joue autour des objectifs, pose de la vision profonde et ping tes coéquipiers pour les rotations."
    else:
        return "Late game: groupe avec ton équipe, joue autour des spikes et protège tes carries en teamfight."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
