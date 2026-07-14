# === Stage 17: Добавь группировку записей по категориям ===
# Project: FleetCare
def group_records_by_category(records, category_field='category'):
    groups = {}
    for rec in records:
        cat = rec.get(category_field, 'Uncategorized')
        if cat not in groups:
            groups[cat] = []
        groups[cat].append(rec)
    return dict(sorted(groups.items(), key=lambda x: len(x[1]), reverse=True))
