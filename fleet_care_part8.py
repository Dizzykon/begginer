# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: FleetCare
def main():
    print("=== FleetCare: Журнал обслуживания транспорта ===")
    while True:
        menu = """
1. Добавить транспорт (марка, модель, пробег)
2. Записать работу/ремонт (дата, описание, стоимость)
3. Зафиксировать расход топлива (объем, цена за литр)
4. Просмотреть историю по автомобилю
5. Вывести сводку расходов и пробега
6. Удалить запись о транспорте
7. Сохранить данные в файл 'fleet_data.txt'
8. Загрузить данные из файла 'fleet_data.txt'
9. Напомнить о плановом ТО (если пробег > 15000)
0. Выход
Выберите действие: """
        choice = input(menu).strip()
        if not choice.isdigit():
            print("Неверный ввод.")
            continue
        action = int(choice)
        if action == 0:
            break
        elif action == 1:
            brand, model, mileage = input("Марка, модель, пробег (км): ").split()
            fleet_data[brand][model] = {"mileage": float(mileage), "works": [], "expenses": []}
            print(f"Транспорт {brand} {model} добавлен.")
        elif action == 2:
            if not fleet_data:
                print("Нет транспорта в системе.")
                continue
            brand, model = input("Марка и модель (через пробел): ").split()
            date, desc, cost = input("Дата (ДД.ММ), описание, стоимость: ").split(',')
            fleet_data[brand][model]["works"].append({"date": date.strip(), "desc": desc.strip(), "cost": float(cost)})
        elif action == 3:
            if not fleet_data:
                print("Нет транспорта в системе.")
                continue
            brand, model = input("Марка и модель (через пробел): ").split()
            volume, price = input("Объем топлива (л), цена за литр: ").split()
            fleet_data[brand][model]["expenses"].append({"volume": float(volume), "price": float(price)})
        elif action == 4:
            if not fleet_data:
                print("Нет транспорта в системе.")
                continue
            brand, model = input("Марка и модель (через пробел): ").split()
            car = fleet_data[brand][model]
            total_mileage = car["mileage"]
            works_count = len(car["works"])
            expenses_count = len(car["expenses"])
            print(f"Пробег: {total_mileage} км, Работы: {works_count}, Расходы: {expenses_count}")
        elif action == 5:
            total_expenses = sum(exp["volume"] * exp["price"] for car in fleet_data.values() for exp in car["expenses"])
            print(f"Общие расходы на топливо: {total_expenses:.2f} руб.")
        elif action == 6:
            brand, model = input("Марка и модель (через пробел): ").split
