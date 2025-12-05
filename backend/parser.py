from flask import Flask, request, jsonify
from flask_cors import CORS

import os
import openai

app = Flask(__name__)
CORS(app)  # autoriser ton frontend (GitHub Pages) à appeler l’API
openai.api_key = os.getenv("OPENAI_API_KEY")


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
    data = request.get_json(silent=True) or {}
    ts = data.get("timestamp")
    context = data.get("context", {})

    if ts is None:
        return jsonify({"error": "timestamp manquant"}), 400

    # Construire le prompt
    prompt = build_prompt(ts, context)

    # Appel à l’IA
    response = openai.ChatCompletion.create(
        model="gpt-4",  # ou gpt-3.5 si tu veux réduire le coût
        messages=[
            {"role": "system", "content": "Tu es un coach League of Legends expert."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300
    )

    advice = response["choices"][0]["message"]["content"]
    return jsonify({"advice": advice, "timestamp": ts})


def simple_coach(ts, context):
    # Exemples basiques que tu remplaceras par ta vraie IA
    if ts < 600:
        return "Early game: concentre-toi sur le last-hit, évite les trades défavorables et garde la wave côté sûr."
    elif ts < 1200:
        return "Mid game: joue autour des objectifs, pose de la vision profonde et ping tes coéquipiers pour les rotations."
    else:
        return "Late game: groupe avec ton équipe, joue autour des spikes et protège tes carries en teamfight."

def build_prompt(ts, context):
    role = context.get("role", "inconnu")
    champion = context.get("champion", "champion inconnu")
    gold = context.get("gold", "non précisé")
    cs = context.get("cs", "non précisé")
    kills = context.get("kills", 0)
    deaths = context.get("deaths", 0)
    items = context.get("items", [])

    return (
        f"À {ts//60}:{ts%60:02d}, le joueur {role} ({champion}) a {gold} gold, "
        f"{cs} CS, {kills} kills et {deaths} morts. Ses items: {', '.join(items)}. "
        "Analyse cette situation et donne un conseil unique et précis pour améliorer son gameplay."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

