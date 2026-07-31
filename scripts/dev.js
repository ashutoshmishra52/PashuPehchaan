const { spawn, spawnSync } = require("child_process");
const fs = require("fs");
const { pythonBin, root, venvDir } = require("./python");

function ensureReady() {
  if (!fs.existsSync(venvDir) || !fs.existsSync(pythonBin())) {
    console.log("→ First run: setting up environment…");
    const setup = spawnSync(process.execPath, [require.resolve("./setup.js")], {
      cwd: root,
      stdio: "inherit",
    });
    if (setup.status !== 0) process.exit(setup.status || 1);
  }
}

ensureReady();

const py = pythonBin();
const args = [
  "-m",
  "uvicorn",
  "app.main:app",
  "--reload",
  "--host",
  "127.0.0.1",
  "--port",
  "8000",
];

console.log("");
console.log("  PashuPehchaan");
console.log("  → http://127.0.0.1:8000");
console.log("  Press Ctrl+C to stop");
console.log("");

const child = spawn(py, args, {
  cwd: root,
  stdio: "inherit",
  env: process.env,
});

child.on("exit", (code) => process.exit(code || 0));
