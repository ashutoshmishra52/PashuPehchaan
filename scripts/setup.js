const { spawnSync } = require("child_process");
const fs = require("fs");
const path = require("path");
const { pythonBin, root, venvDir } = require("./python");

function run(cmd, args, opts = {}) {
  const result = spawnSync(cmd, args, {
    cwd: root,
    stdio: "inherit",
    shell: process.platform === "win32",
    ...opts,
  });
  return result.status === 0;
}

function runOrExit(cmd, args) {
  if (!run(cmd, args)) {
    console.error(`✗ Failed: ${cmd} ${args.join(" ")}`);
    process.exit(1);
  }
}

function ensureVenv() {
  if (fs.existsSync(venvDir) && fs.existsSync(pythonBin())) return;

  console.log("→ Creating Python virtualenv…");
  const candidates =
    process.platform === "win32" ? ["python", "py", "python3"] : ["python3", "python"];

  let created = false;
  for (const cmd of candidates) {
    const ok = run(cmd, ["-m", "venv", ".venv"]);
    if (ok && fs.existsSync(pythonBin())) {
      created = true;
      break;
    }
  }

  if (!created) {
    console.error("✗ Python 3.9+ not found. Install Python and retry.");
    process.exit(1);
  }
}

ensureVenv();

const py = pythonBin();
console.log("→ Installing Python packages (torch may take a few minutes)…");
runOrExit(py, ["-m", "pip", "install", "--upgrade", "pip"]);
runOrExit(py, ["-m", "pip", "install", "-r", "requirements.txt"]);

// Warn if model is missing / LFS pointer
const modelPath = path.join(root, "models", "Indian_bovine_finetuned_model.pth");
if (!fs.existsSync(modelPath)) {
  console.warn("⚠ Model file missing. It will download from Hugging Face on first run (needs internet).");
} else {
  const size = fs.statSync(modelPath).size;
  if (size < 2048) {
    console.warn(
      "⚠ Model looks like a Git LFS pointer. Run: git lfs install && git lfs pull\n" +
        "  Or just start the app — it can auto-download from Hugging Face."
    );
  } else {
    console.log(`✓ AI model present (${Math.round(size / (1024 * 1024))} MB)`);
  }
}

console.log("✓ Setup complete. Run: npm run dev");
