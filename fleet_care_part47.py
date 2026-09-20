# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: FleetCare
def demo():
    print("=" * 60)
    print("DEMO: FleetCare — Журнал обслуживания транспорта")
    print("=" * 60)

    # 1. Инициализация автопарка
    fleet = FleetManager()
    fleet.add_vehicle("Toyota Camry", "ABC-123", "2020-01-15")
    fleet.add_vehicle("Ford Transit", "XYZ-789", "2019-06-01")
    fleet.add_vehicle("Hyundai Solaris", "DEF-456", "2021-03-10")
    print(f"\nАвтомобилей в парке: {len(fleet.vehicles)}")

    # 2. Пробеги
    for name, plate in fleet.vehicles:
        fleet.record_mileage(name, plate, fleet.current_mileage(name, plate) + 5000)
    print("Пробег каждого авто увеличен на 5000 км.")

    # 3. Расходы
    for name, plate in fleet.vehicles:
        fleet.add_expense(name, plate, 350.0, "Заправка")
    print("Добавлены расходы по заправке.")

    # 4. Ремонты
    fleet.add_maintenance("Toyota Camry", "ABC-123", "Ремонт тормозов", "2023-11-20", 15000.0)
    fleet.add_maintenance("Ford Transit", "XYZ-789", "Замена масла", "2023-12-05", 2500.0)
    print("Добавлены работы по ремонту.")

    # 5. Напоминания
    for name, plate in fleet.vehicles:
        fleet.add_reminder(name, plate, "Замена масла", "2024-01-15")
    print("Добавлены напоминания о ТО.")

    # 6. Отчёт
    print("\n--- Отчёт по автопарку ---")
    for name, plate, odometer in fleet.vehicles:
        print(f"  {name} ({plate}): пробег = {odometer} км")
    print(f"  Общее количество расходов: {fleet.total_expenses} руб.")
    print(f"  Всего выполнено работ: {fleet.total_maintenance_count} шт.")
    print(f"  Активных напоминаний: {fleet.active_reminders} шт.")

    print("\nDEMO завершён. Спасибо за использование FleetCare!")
