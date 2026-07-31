# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: FleetCare
def reset_demo_data():
    """Сбрасывает все данные в дефолты для демонстрации."""
    global fleet, maintenance_log, expenses, reminders, current_mileage, total_spent
    
    fleet = [
        {"id": 1, "brand": "Toyota", "model": "Camry", "year": 2021},
        {"id": 2, "brand": "Ford", "model": "F-150", "year": 2020},
    ]
    maintenance_log = []
    expenses = []
    reminders = []
    current_mileage = {1: 45000, 2: 62000}
    total_spent = 0
    
    print("✅ Демо-данные сброшены. Готов к началу нового цикла.")

def clear_state():
    """Полностью очищает все данные и сбрасывает состояние."""
    global fleet, maintenance_log, expenses, reminders, current_mileage, total_spent
    
    fleet = []
    maintenance_log = []
    expenses = []
    reminders = []
    current_mileage = {}
    total_spent = 0
    
    print("🧹 Состояние полностью очищено. Начните заново.")
