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
  if (result.status !== 0) {
    process.exit(result.status || 1);
  }
}

if (!fs.existsSync(venvDir)) {
  console.log("→ Creating Python virtualenv…");
  run("python3", ["-m", "venv", ".venv"]);
  // Windows fallback if python3 missing
  if (!fs.existsSync(venvDir)) {
    run("python", ["-m", "venv", ".venv"]);
  }
}

console.log("→ Installing Python packages…");
run(pythonBin(), ["-m", "pip", "install", "-r", "requirements.txt"]);

console.log("✓ Setup complete. Run: npm run dev");
