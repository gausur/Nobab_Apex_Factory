import json
import base64
from PIL import Image
from PIL.PngImagePlugin import PngInfo
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

REPO_NAME = input("Enter your GitHub repo name: ").strip()

mission = {
    "MISSION": "BUILD_18_LAYERS",
    "RULES": "NO_HF, TOR_CHAIN, OBFUSCATE",
    "WORK_CYCLE": "5h_work,1h_sleep",
    "LAYERS": {
        "1": "data_engine", "2": "rag", "3": "agentic_soc", "4": "active_defense",
        "5": "retaliatory", "6": "binary_harden", "7": "kernel", "8": "hyperv",
        "9": "firmware", "10": "microarch", "11": "supply_chain", "12": "quantum",
        "13": "ai_defense", "14": "human_centric", "15": "counter_strike",
        "16": "hyper_attribution", "17": "global_data", "18": "autonomous"
    },
    "REQUIRE_API_KEYS": ["GROQ", "OPENROUTER", "KAGGLE"]
}

plain = json.dumps(mission)
key = f"nobab2026+{REPO_NAME}".encode()[:32]
iv = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
ct, tag = cipher.encrypt_and_digest(plain.encode())
encrypted = base64.b64encode(iv + ct + tag).decode()

img = Image.new('RGB', (200, 200), color='white')
meta = PngInfo()
meta.add_text("XPComment", encrypted)
img.save("nobab_vision.png", pnginfo=meta)

print("✅ nobab_vision.png created successfully!")
print(f"🔑 Key used: {key.decode()}")
