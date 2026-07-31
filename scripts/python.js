const fs = require("fs");
const path = require("path");

const root = path.join(__dirname, "..");
const venvDir = path.join(root, ".venv");

function pythonBin() {
  const win = process.platform === "win32";
  const candidate = win
    ? path.join(venvDir, "Scripts", "python.exe")
    : path.join(venvDir, "bin", "python");
  if (fs.existsSync(candidate)) return candidate;
  // Fallback names
  const alt = win
    ? path.join(venvDir, "Scripts", "python3.exe")
    : path.join(venvDir, "bin", "python3");
  return fs.existsSync(alt) ? alt : candidate;
}

module.exports = { root, venvDir, pythonBin };
