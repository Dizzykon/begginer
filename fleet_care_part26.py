# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: FleetCare
def demo_fleetcare():
    """Quick manual test entry point."""
    from fleetcare import Vehicle, ServiceRecord, FuelLog, Reminder, App
    app = App()
    
    # 1 vehicle
    v = Vehicle("UA-AB-0783", "2021", make="Hyundai", model="Solaris")
    app.add_vehicle(v)
    
    # service log
    app.log_service(v, "Oil change", cost=500.0, km=45000)
    app.log_service(v, "Brake pads", cost=1200.0, km=67000)
    
    # fuel log
    app.log_fuel(v, 38.5, price=42.0)
    app.log_fuel(v, 41.0, price=43.5)
    
    # reminders
    app.remind(v, "Check brakes", "km>70000")
    app.remind(v, "Insurance expiring", "date<2026-01-15")
    
    print("=== FleetCare Demo ===")
    for rec in v.service_log:
        print(f"[Service] {rec.description} at {rec.km} km - cost {rec.cost}")
    for rec in v.fuel_log:
        print(f"[Fuel]   {rec.liters:.1f}L @ {rec.price} UAH/L")
    for r in v.reminders:
        print(f"[Remind] {r.message} (trigger: {r.trigger})")
    
    total_cost = sum(r.cost for r in v.service_log)
    avg_price = sum(f.price * f.liters for f in v.fuel_log) / sum(f.liters for f in v.fuel_log) if v.fuel_log else 0
    print(f"\n[Summary] Total service cost: {total_cost:.2f} UAH")
    print(f"[Summary] Avg fuel price:     {avg_price:.2f} UAH/L")

if __name__ == "__main__":
    demo_fleetcare()
