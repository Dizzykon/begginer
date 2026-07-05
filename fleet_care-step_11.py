# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: FleetCare
import json, os

DATA_FILE = "fleetcare_data.json"

def save_to_json(data):
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except IOError as e:
        print(f"[Ошибка] Не удалось сохранить данные в {DATA_FILE}: {e}")

def load_from_json():
    if not os.path.exists(DATA_FILE):
        return {"vehicles": [], "logs": []}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError):
        print("[Предупреждение] Файл данных повреждён или отсутствует. Используются пустые данные.")
        return {"vehicles": [], "logs": []}

def get_data():
    data = load_from_json()
    if not os.path.exists(DATA_FILE) or len(data.get("vehicles", [])) == 0:
        save_to_json({"vehicles": [], "logs": []})
    return data
