# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: FleetCare
def weekly_stats(records, start_date):
    """Расчёт недельной статистики (средний пробег/неделю) начиная с даты."""
    from datetime import timedelta
    week = [start_date + timedelta(days=d) for d in range(7)]
    stats = {d: [] for d in week}
    for r in records:
        if start_date <= r['date'] < start_date + timedelta(days=7):
            stats[r['date']].append(r)
    return {d.strftime('%Y-%m-%d'): {'count': len(v), 'total_km': sum(x.get('odometer', 0) for x in v)} for d, v in stats.items()}
