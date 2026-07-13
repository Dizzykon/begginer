# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: FleetCare
def monthly_stats(records, year=None):
    if not records:
        return []
    from datetime import date
    grouped = {}
    for rec in records:
        d = rec['date']
        if year is not None:
            key = (year, d.month)
        else:
            key = (d.year, d.month)
        grouped.setdefault(key, []).append(rec)
    result = []
    for month in range(1, 13):
        data = grouped.get((year or date.today().year), month)
        if not data:
            continue
        total_km = sum(r['odometer'] - r.get('prev_odometer', 0) for r in data)
        result.append({
            'month': month,
            'records_count': len(data),
            'total_km': total_km,
        })
    return result
