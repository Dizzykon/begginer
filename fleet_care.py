# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: FleetCare
def main():
    fleet = {
        "vehicles": [
            {"id": 1, "model": "Toyota Camry", "mileage": 45000},
            {"id": 2, "model": "Ford Transit", "mileage": 82000}
        ],
        "records": []
    }

    def add_record(vehicle_id, type_, value):
        fleet["records"].append({
            "vehicle_id": vehicle_id,
            "type": type_,
            "value": value,
            "date": datetime.now().strftime("%Y-%m-%d")
        })

    # Демонстрация: добавление записи о ТО для первого автомобиля
    add_record(1, "maintenance", 50)
    
    print(f"Текущий пробег Toyota Camry: {fleet['vehicles'][0]['mileage']} км")
    print(f"История записей:\n{fleet['records']}")

if __name__ == "__main__":
    main()
