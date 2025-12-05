const input = document.getElementById("replayInput");
const output = document.getElementById("output");

input.addEventListener("change", async () => {
  const file = input.files[0];
  if (!file) return;

  const formData = new FormData();
  formData.append("file", file);

 const response = await fetch("https://coach-lol-backend.onrender.com/upload", {
  method: "POST",
  body: formData
});

  const data = await response.json();
  output.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
});
