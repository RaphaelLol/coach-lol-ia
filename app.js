const input = document.getElementById("replayInput");
const output = document.getElementById("output");

input.addEventListener("change", () => {
  const file = input.files[0];
  if (!file) return;
  output.innerHTML = `<p>✅ Fichier importé : <strong>${file.name}</strong></p>`;
  // Ici tu ajouteras plus tard le parsing du .ROFL
});
