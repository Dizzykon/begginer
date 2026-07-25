# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: FleetCare
def print_vehicle_table(fleet):
    headers = ["ID", "Марка/Модель", "КМ (тыс.)", "Последняя работа", "Дата"]
    width = [10, 25, 20, 35, 18]
    fmts = ["{:>10}", "{:<25}", "{:>20}", "{:<35}", "{:18}"]
    
    print(f"\n{'─'*96}\n")
    for i, h in enumerate(headers):
        print(fmts[i].format(h).center(width[i], "─"), end="")
    print()
    print("│" + "├" * 84 + "│")
    
    for v in fleet:
        row = [v.id, f"{v.make} {v.model}", f"{v.odometer/1000:.2f}", 
               str(v.last_service) if v.last_service else "-", v.date_str]
        print("│" + "├".join(fmts[i].format(row[i]) for i in range(5)) + "│")

if __name__ == "__main__":
    print_vehicle_table(fleet)
