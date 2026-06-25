# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: FleetCare
def edit_record(record_id, updates):
    if record_id not in records:
        print(f"Запись с ID {record_id} не найдена.")
        return False
    for key, value in updates.items():
        if hasattr(records[record_id], key):
            setattr(records[record_id], key, value)
        else:
            print(f"Свойство '{key}' недоступно для редактирования.")
            return False
    save_to_file()
    print(f"Запись {record_id} успешно обновлена.")
    return True
