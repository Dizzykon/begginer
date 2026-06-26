# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: FleetCare
def delete_record(record_id, record_type):
    if not isinstance(record_id, int) or record_id <= 0:
        raise ValueError("ID должен быть положительным целым числом")
    
    try:
        if record_type == "trip":
            fleet_cars[record_id]["trips"].pop()
        elif record_type == "maintenance":
            fleet_cars[record_id]["maintenances"].pop()
        elif record_type == "expense":
            fleet_cars[record_id]["expenses"].pop()
        elif record_type == "reminder":
            fleet_cars[record_id]["reminders"].pop()
        else:
            raise ValueError(f"Неизвестный тип записи: {record_type}")
    except IndexError:
        print(f"Запись с ID {record_id} для типа '{record_type}' не найдена.")

def get_record_by_id(record_id, record_type):
    if not isinstance(record_id, int) or record_id <= 0:
        return None
    
    try:
        if record_type == "trip":
            return fleet_cars[record_id]["trips"][-1]
        elif record_type == "maintenance":
            return fleet_cars[record_id]["maintenances"][-1]
        elif record_type == "expense":
            return fleet_cars[record_id]["expenses"][-1]
        elif record_type == "reminder":
            return fleet_cars[record_id]["reminders"][-1]
    except (IndexError, KeyError):
        pass
    
    return None
