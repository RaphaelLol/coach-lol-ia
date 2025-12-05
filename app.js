// Config backend
const BACKEND_URL = "https://coach-lol-backend.onrender.com";

// Elements
const fileInput = document.getElementById("video-input");
const loadBtn = document.getElementById("load-video");
const videoEl = document.getElementById("replay");
const back10Btn = document.getElementById("back-10");
const forward10Btn = document.getElementById("forward-10");
const timeReadout = document.getElementById("time-readout");
const askAiBtn = document.getElementById("ask-ai");
const aiResult = document.getElementById("ai-result");

// Charger la vidéo locale dans le lecteur
loadBtn.addEventListener("click", () => {
  const file = fileInput.files?.[0];
  if (!file) {
    alert("Sélectionne un fichier .mp4");
    return;
  }
  const url = URL.createObjectURL(file);
  videoEl.src = url;
  videoEl.load();
  videoEl.play();
});

// Mise à jour de l’affichage du temps
function formatTime(seconds) {
  const s = Math.floor(seconds % 60);
  const m = Math.floor((seconds / 60) % 60);
  const h = Math.floor(seconds / 3600);
  const mm = String(m).padStart(2, "0");
  const ss = String(s).padStart(2, "0");
  return h > 0 ? `${h}:${mm}:${ss}` : `${mm}:${ss}`;
}

videoEl.addEventListener("timeupdate", () => {
  timeReadout.textContent = formatTime(videoEl.currentTime);
});

// Contrôles -10s / +10s
back10Btn.addEventListener("click", () => {
  videoEl.currentTime = Math.max(0, videoEl.currentTime - 10);
});
forward10Btn.addEventListener("click", () => {
  const newTime = Math.min(videoEl.duration || videoEl.currentTime + 10, videoEl.currentTime + 10);
  videoEl.currentTime = newTime;
});

// Demander un conseil IA pour le timestamp actuel
askAiBtn.addEventListener("click", async () => {
  const timestampSeconds = Math.floor(videoEl.currentTime);
  aiResult.textContent = "Analyse en cours...";
  try {
    // Envoie le timestamp + métadonnées basiques (tu pourras enrichir)
    const payload = {
      timestamp: timestampSeconds,
      // Optionnel: ajoute des champs comme champion, lane, rôle, etc.
      context: {
        source: "video",
        duration: Math.floor(videoEl.duration || 0)
      }
    };
    const res = await fetch(`${BACKEND_URL}/analyze`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();
    aiResult.textContent = data.advice || "Pas de conseil renvoyé.";
  } catch (err) {
    aiResult.textContent = "Erreur d'analyse IA. Réessaie.";
    console.error(err);
  }
});
