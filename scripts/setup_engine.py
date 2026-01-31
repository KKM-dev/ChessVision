import os
import platform
import zipfile
import urllib.request
import shutil

STOCKFISH_VERSION = "16"
ENGINE_DIR = "engine"

WINDOWS_URL = (
    "https://github.com/official-stockfish/Stockfish/releases/"
    "download/sf_16/stockfish-windows-x86-64-avx2.zip"
)

def download_stockfish():
    print("🔽 Downloading Stockfish...")
    zip_path = "stockfish.zip"
    urllib.request.urlretrieve(WINDOWS_URL, zip_path)
    return zip_path

def extract_engine(zip_path):
    print("📦 Extracting engine...")
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall("temp_stockfish")

def setup_engine():
    if not os.path.exists(ENGINE_DIR):
        os.makedirs(ENGINE_DIR)

    system = platform.system()

    if system != "Windows":
        raise RuntimeError("Only Windows is supported in v1")

    zip_path = download_stockfish()
    extract_engine(zip_path)

    # Find stockfish executable
    for root, _, files in os.walk("temp_stockfish"):
        for file in files:
            if file.lower().startswith("stockfish") and file.endswith(".exe"):
                src = os.path.join(root, file)
                dst = os.path.join(ENGINE_DIR, "stockfish.exe")
                shutil.move(src, dst)
                break

    shutil.rmtree("temp_stockfish")
    os.remove(zip_path)

    print("✅ Stockfish setup complete.")
    print("📁 Engine located at: engine/stockfish.exe")

if __name__ == "__main__":
    setup_engine()
