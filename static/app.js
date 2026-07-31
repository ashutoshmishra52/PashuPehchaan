const fileInput = document.getElementById("file-input");
const dropzone = document.getElementById("dropzone");
const dropIdle = document.getElementById("drop-idle");
const dropReady = document.getElementById("drop-ready");
const preview = document.getElementById("preview");
const fileName = document.getElementById("file-name");
const actions = document.getElementById("actions");
const form = document.getElementById("upload-form");
const predictBtn = document.getElementById("predict-btn");
const clearBtn = document.getElementById("clear-btn");
const resultEl = document.getElementById("result");
const statusEl = document.getElementById("status");
const statusText = document.getElementById("status-text");
const topbar = document.getElementById("topbar");

let selectedFile = null;
let previewUrl = null;
let toastTimer = null;
let allBreeds = [];

function showStatus(msg, isError = false) {
  statusText.textContent = msg;
  statusEl.hidden = false;
  statusEl.classList.toggle("error", isError);
  requestAnimationFrame(() => statusEl.classList.add("is-visible"));
  clearTimeout(toastTimer);
  toastTimer = setTimeout(hideStatus, 3800);
}

function hideStatus() {
  statusEl.classList.remove("is-visible");
  setTimeout(() => {
    if (!statusEl.classList.contains("is-visible")) statusEl.hidden = true;
  }, 350);
}

function setPreview(file) {
  if (previewUrl) URL.revokeObjectURL(previewUrl);
  selectedFile = file;
  previewUrl = URL.createObjectURL(file);
  preview.src = previewUrl;
  preview.alt = "Selected photo";
  fileName.textContent = file.name;
  dropIdle.hidden = true;
  dropReady.hidden = false;
  actions.hidden = false;
  resultEl.hidden = true;
  hideStatus();
}

function clearPreview() {
  if (previewUrl) URL.revokeObjectURL(previewUrl);
  selectedFile = null;
  previewUrl = null;
  fileInput.value = "";
  preview.removeAttribute("src");
  preview.alt = "";
  fileName.textContent = "";
  dropIdle.hidden = false;
  dropReady.hidden = true;
  actions.hidden = true;
  resultEl.hidden = true;
  hideStatus();
}

window.addEventListener(
  "scroll",
  () => {
    topbar.classList.toggle("is-scrolled", window.scrollY > 40);
  },
  { passive: true }
);

dropzone.addEventListener("dragover", (e) => {
  e.preventDefault();
  dropzone.classList.add("dragover");
});

dropzone.addEventListener("dragleave", () => {
  dropzone.classList.remove("dragover");
});

dropzone.addEventListener("drop", (e) => {
  e.preventDefault();
  dropzone.classList.remove("dragover");
  const file = e.dataTransfer.files?.[0];
  if (file && file.type.startsWith("image/")) setPreview(file);
  else showStatus("Please drop an image file.", true);
});

fileInput.addEventListener("change", () => {
  const file = fileInput.files?.[0];
  if (file) setPreview(file);
});

clearBtn.addEventListener("click", (e) => {
  e.preventDefault();
  e.stopPropagation();
  clearPreview();
});

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  if (!selectedFile) {
    showStatus("Choose a photo first.", true);
    return;
  }

  predictBtn.disabled = true;
  predictBtn.classList.add("is-loading");
  predictBtn.querySelector(".btn-label").textContent = "Analyzing with AI…";
  hideStatus();

  const body = new FormData();
  body.append("file", selectedFile);

  try {
    const res = await fetch("/api/predict", { method: "POST", body });
    const data = await res.json();
    if (!res.ok) {
      const detail = Array.isArray(data.detail) ? data.detail[0]?.msg : data.detail;
      throw new Error(detail || "Prediction failed");
    }
    renderResult(data);
  } catch (err) {
    showStatus(err.message || "Something went wrong.", true);
  } finally {
    predictBtn.disabled = false;
    predictBtn.classList.remove("is-loading");
    predictBtn.querySelector(".btn-label").textContent = "Identify breed";
  }
});

function renderResult(data) {
  document.getElementById("breed-name").textContent = data.breed;
  document.getElementById("breed-meta").textContent =
    `${data.animal_type} · ${data.details.region}`;
  document.getElementById("breed-desc").textContent = data.details.description;

  const uploadImg = document.getElementById("result-upload");
  uploadImg.src = previewUrl || "";

  const fill = document.getElementById("conf-fill");
  const label = document.getElementById("conf-label");
  fill.style.width = "0%";
  label.textContent = `${data.confidence}%`;
  requestAnimationFrame(() => {
    requestAnimationFrame(() => {
      fill.style.width = `${data.confidence}%`;
    });
  });

  document.getElementById("breed-facts").innerHTML = `
    <div><dt>Milk yield</dt><dd>${data.details.milk_yield}</dd></div>
    <div><dt>Lifespan</dt><dd>${data.details.lifespan}</dd></div>
    <div><dt>Usage</dt><dd>${data.details.usage}</dd></div>
    <div><dt>Region</dt><dd>${data.details.region}</dd></div>
  `;

  const alts = document.getElementById("alts");
  if (data.alternatives?.length) {
    alts.innerHTML = `
      <h3>Other likely matches</h3>
      ${data.alternatives
        .map(
          (a) => `
        <div class="alt-row">
          <span>${a.breed} <small>(${a.type})</small></span>
          <span class="alt-conf">${a.confidence}%</span>
        </div>`
        )
        .join("")}
    `;
  } else {
    alts.innerHTML = "";
  }

  resultEl.hidden = false;
  const panel = resultEl.querySelector(".result-panel");
  panel.style.animation = "none";
  void panel.offsetWidth;
  panel.style.animation = "";
  resultEl.scrollIntoView({ behavior: "smooth", block: "start" });
}

function renderBreedGrid(filter = "all") {
  const grid = document.getElementById("breed-grid");
  grid.innerHTML = allBreeds
    .map((b, i) => {
      const hidden = filter !== "all" && b.type !== filter;
      return `
      <article class="breed-card${hidden ? " is-hidden" : ""}" style="animation-delay:${i * 0.04}s" data-type="${b.type}">
        <div class="body">
          <span class="tag">${b.type}</span>
          <div class="name">${b.name}</div>
          <div class="sub">${b.region}</div>
          <div class="yield">${b.milk_yield}</div>
        </div>
      </article>`;
    })
    .join("");
}

document.querySelectorAll(".filter").forEach((btn) => {
  btn.addEventListener("click", () => {
    document.querySelectorAll(".filter").forEach((b) => b.classList.remove("is-active"));
    btn.classList.add("is-active");
    renderBreedGrid(btn.dataset.filter);
  });
});

async function loadBreeds() {
  try {
    const res = await fetch("/api/breeds");
    const data = await res.json();
    allBreeds = data.breeds || [];
    renderBreedGrid("all");
  } catch {
    showStatus("Could not load breed library.", true);
  }
}

loadBreeds();
