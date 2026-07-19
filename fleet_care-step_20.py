# === Stage 20: Добавь восстановление записей из архива ===
# Project: FleetCare
def restore_archive(records, archive_path="archive.json"):
    """Восстановить записи из архива в основной список."""
    import json
    with open(archive_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                try:
                    records.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
