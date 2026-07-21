# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: FleetCare
class Reminder:
    """Простое напоминание с датой выполнения."""
    
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
    
    def is_due(self, current_date=None):
        if current_date is None:
            from datetime import date
            current_date = date.today()
        return current_date >= self.due_date
    
    def __repr__(self):
        status = "🟢 выполнено" if self.is_due() else "⏳ ожидается"
        return f"<Reminder [{status}] {self.description} до: {self.due_date}>"


# Пример использования с текущей датой
from datetime import date, timedelta

# Создаём напоминание на 3 дня от сегодня
reminder = Reminder("Замена масла", date.today() + timedelta(days=3))
print(reminder)
