# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: FleetCare
import json, sys

def load_initial_data(json_string: str) -> dict:
    try:
        data = json.loads(json_string)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект")
        
        # Валидация структуры данных
        required_keys = ['vehicles', 'maintenance_logs', 'expenses']
        for key in required_keys:
            if key not in data:
                raise KeyError(f"Отсутствует обязательное поле: {key}")
            
            if not isinstance(data[key], list):
                raise TypeError(f"Поле '{key}' должно быть списком")
        
        # Проверка типов внутри записей (пример)
        for log in data['maintenance_logs']:
            if 'vehicle_id' not in log or 'date' not in log:
                raise ValueError("Некорректая запись в maintenance_logs")
                
        return data
        
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка загрузки данных: {e}")
        sys.exit(1)

# Пример использования (раскомментируйте для теста):
if __name__ == "__main__":
    sample_json = '''
    {
        "vehicles": [{"id": 1, "model": "Toyota Camry", "mileage": 50000}],
        "maintenance_logs": [{"vehicle_id": 1, "date": "2023-10-01", "work": "Замена масла"}],
        "expenses": [{"vehicle_id": 1, "amount": 500.0, "category": "oil_change"}]
    }'''
    
    fleet_data = load_initial_data(sample_json)
    print(f"Загружено {len(fleet_data['vehicles'])} транспортных средств.")
