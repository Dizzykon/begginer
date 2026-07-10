# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: FleetCare
def print_summary():
    """Выводит краткую сводку по текущим данным."""
    total_miles = sum(car.mileage for car in cars) if cars else 0
    total_fuel_cost = sum(expense.cost for expense in expenses if expense.category == "fuel") if expenses else 0
    upcoming_services = [svc for svc in services if svc.date <= datetime.now().date() and not svc.done] if services else []

    print(f"=== FleetCare Summary ===")
    print(f"Cars: {len(cars)} | Total mileage: {total_miles} mi")
    print(f"Fuel spent: ${total_fuel_cost:.2f}")
    if upcoming_services:
        print(f"\nUpcoming services ({len(upcoming_services)}):")
        for svc in upcoming_services:
            print(f"  - {svc.vehicle_name}: {svc.description} (due {svc.date})")
    else:
        print("\nNo upcoming services.")

if __name__ == "__main__":
    # Пример данных для тестирования
    cars = [Car("Toyota Camry", "ABC123", 5000), Car("Honda Civic", "XYZ789", 3200)]
    expenses = [Expense("fuel", 45.0, 500), Expense("oil change", 60.0, 1000)]
    services = [Service("ABC123", "Oil filter replacement", datetime(2024, 7, 15)), Service("XYZ789", "Brake inspection", datetime(2024, 8, 1))]

    print_summary()
