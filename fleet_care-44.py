# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: FleetCare
import shutil, os, datetime

def backup_log(log_path):
    if not os.path.exists(log_path):
        return
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = f"{log_path}.backup_{ts}"
    shutil.copy2(log_path, backup_path)
    print(f"Бэкап создан: {backup_path}")
    return backup_path
