# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: FleetCare
def filter_records(status=None, category=None, tags=None):
    filtered = []
    for record in records:
        if status and record.get('status') != status:
            continue
        if category and record.get('category') != category:
            continue
        if tags is not None:
            rec_tags = record.get('tags', [])
            if isinstance(tags, str):
                tags = [tags]
            if not any(t in rec_tags for t in tags):
                continue
        filtered.append(record)
    return filtered
