# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: FleetCare
def next_action(s):
    if not s:
        return "Начните с добавления первого автомобиля."
    if s.get("next_maintenance"):
        return f"Запланируйте обслуживание через {s['next_maintenance']} км."
    if s.get("alerts"):
        return "Рассмотрите рекомендации из активных предупреждений."
    if s.get("expenses"):
        return "Проанализируйте расходы за последний месяц."
    if s.get("vehicles"):
        return "Обновите данные по пробегу для всех автомобилей."
    return "Синхронизируйте данные с базой."
