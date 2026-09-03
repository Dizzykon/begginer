# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: FleetCare
def repair_simple_issues(records):
    """Проверяет целостность записей и пытается исправить простые проблемы."""
    errors = []
    for i, rec in enumerate(records):
        if not isinstance(rec, dict):
            errors.append(f"Запись {i}: не словарь")
            continue
        if "id" not in rec:
            rec["id"] = i
        if "date" not in rec:
            rec["date"] = "2024-01-01"
        if "mileage" not in rec:
            rec["mileage"] = 0
        if "cost" not in rec:
            rec["cost"] = 0.0
        if rec.get("mileage", 0) < 0:
            rec["mileage"] = 0
        if rec.get("cost", 0) < 0:
            rec["cost"] = 0.0
    return errors
