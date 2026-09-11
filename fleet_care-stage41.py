# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: FleetCare
def dry_run(operation, record_id, original_data, new_data):
    """Симуляция операции изменения данных без применения."""
    print(f"[DRY-RUN] Операция: {operation}")
    print(f"  Record ID: {record_id}")
    print(f"  Изменено: {original_data} -> {new_data}")
    print(f"  Статус: не применено")
    return {"applied": False, "operation": operation, "record_id": record_id, "original": original_data, "new": new_data}

# Пример использования
result = dry_run("update_mileage", 1, {"mileage": 1000}, {"mileage": 1500})
print(result)
