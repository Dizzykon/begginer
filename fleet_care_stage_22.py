# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: FleetCare
def check_overdue_reminders():
    today = datetime.date.today()
    overdue = []
    for entry in reminders:
        if entry['date'] < today and 'done' not in entry and 'overdue' not in entry:
            entry['overdue'] = True
            entry['days_overdue'] = (today - entry['date']).days
            overdue.append(entry)
    return overdue
