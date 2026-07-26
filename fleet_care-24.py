# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: FleetCare
def print_record(record):
    """Компактный вывод одной записи с деталями."""
    if not record:
        return "Нет данных."
    
    parts = []
    for key, val in record.items():
        label = key.replace("_", " ").title()
        parts.append(f"{label}: {val}")
    
    print("─" * 40)
    print(" ".join(parts))
