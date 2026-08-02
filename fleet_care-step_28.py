# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: FleetCare
def print_metrics(records, expenses, reminders):
    """Добавить блок подсчёта ключевых метрик в конец файла."""
    total_mileage = sum(r.mileage for r in records)
    avg_mileage_per_record = (
        total_mileage / len(records) if records else 0
    )

    completed_works = [r for r in records if r.status == "completed"]
    pending_works = [r for r in records if r.status == "pending"]

    total_expense = sum(e.cost for e in expenses)
    avg_cost_per_job = (
        total_expense / len(completed_works) if completed_works else 0
    )

    urgent_reminders = [
        r for r in reminders if r.urgent and r.date <= datetime.now()
    ]
    upcoming_reminders = [
        r for r in reminders if not r.urgent and r.date > datetime.now()
    ]

    print("=" * 40)
    print("📊 FleetCare — Ключевые метрики")
    print(f"   Всего записей: {len(records)}")
    print(f"   Общий пробег: {total_mileage:.1f} км")
    print(f"   Средний пробег/запись: {avg_mileage_per_record:.1f} км")
    print(f"   Завершено работ: {len(completed_works)}")
    print(f"   В работе: {len(pending_works)}")
    if total_expense > 0:
        print(f"   Средний расход/работу: {avg_cost_per_job:.2f} руб.")
    print(f"   Срочные напоминания: {len(urgent_reminders)}")
    print(f"   Ближайшие напоминания: {len(upcoming_reminders)}")
    print("=" * 40)


# Пример вызова (раскомментируй после заполнения данных):
# if __name__ == "__main__":
#     records = [...]
#     expenses = [...]
#     reminders = [...]
#     print_metrics(records, expenses, reminders)
