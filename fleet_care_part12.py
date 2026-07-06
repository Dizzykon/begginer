# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: FleetCare
def load_from_json(filepath):
    """Загружает данные из JSON-файла с обработкой ошибок."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            print(f"[FleetCare] Загрузлено {len(data)} записей из '{filepath}'.")
            return data
    except FileNotFoundError:
        print(f"[FleetCare] Ошибка: файл '{filepath}' не найден.")
        return None
    except json.JSONDecodeError as e:
        print(f"[FleetCare] Ошибка формата JSON в '{filepath}': {e}")
        return None
    except PermissionError:
        print(f"[FleetCare] Недостаточно прав для чтения '{filepath}'.")
        return None
