# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: FleetCare
def export_to_json():
    import json
    from datetime import datetime
    data = {
        "fleet": fleet,
        "vehicles": vehicles,
        "maintenance_logs": maintenance_logs,
        "expenses": expenses,
        "reminders": reminders,
        "exported_at": datetime.now().isoformat()
    }
    return json.dumps(data, indent=2)
