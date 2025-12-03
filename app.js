const input = document.getElementById("replayInput");
const output = document.getElementById("output");

input.addEventListener("change", async () => {
  const file = input.files[0];
  if (!file) return;

  const formData = new FormData();
  formData.append("file", file);

  // Envoi du fichier au backend Flask
  const response = await fetch("http://localhost:5000/upload", {
    method: "POST",
    body: formData
  });

  const data = await response.json();
  output.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
});
