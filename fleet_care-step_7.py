# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: FleetCare
def sort_records(records, key='date', reverse=False):
    if not records: return []
    order = {'date': lambda r: (r['created_at'] or '')[:10], 'priority': lambda r: -int(r.get('priority', 3)), 'name': lambda r: r['name'].lower()}
    key_func = order.get(key, order['date'])
    return sorted(records, key=key_func, reverse=reverse)

def filter_and_sort_records(records, filters=None):
    if not records or not filters: return sort_records(records)
    filtered = [r for r in records if all(str(r.get(k)) == str(v) for k, v in filters.items())]
    return sort_records(filtered, key=filters.get('sort', 'date'), reverse=filters.get('reverse', False))
